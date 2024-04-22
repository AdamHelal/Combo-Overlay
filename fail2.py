from inputs import get_gamepad
import time, Interface, threading
keepPlaying = True
mapping={}
transactions=[]
transaction=[]
controller=Interface.PSFOUR(mapping)

lock = threading.Lock()


def process_transaction(transaction,recent,event):
    with lock:
        transaction.append(event)
    recent['val'] = event
    recent['time'] = time.time()

def fetch_button_val(event):
    button={'val':'','time':''}
    button['time']=time.time()
    button['val']=controller.fetch_button_val(event)
    return button

def process_input():
    global transaction
    while keepPlaying:
        events = get_gamepad()
        for event in events:
            recent={'val':'','time':''}
            if event.code =='SYN_REPORT': continue
            if event.state == 0 : continue
            # print(event.ev_type, event.code, event.state)
            button=fetch_button_val(event)
            if (recent['time']!='' and (recent['time']==button['time'] or float(button['time'])-float(recent['time']) < 0.2) 
            and button['val'] == recent['val']) or button['val']=='':
                continue
            process_transaction(transaction,recent,button['val'])

def end_transaction():
    global transaction
    while keepPlaying:
        start_time = time.time()  # Get the current time in seconds
        end_time = start_time + 3  # Calculate the time when the action should stop
        while time.time() < end_time:
            time.sleep(0.1)
        print(transaction)
        print(transactions)
        if len(transaction) > 0: transactions.append(transaction)
        with lock:
            transaction=[]
       

def main():
    """Just print out some event infomation when the gamepad is used."""
    input_thread = threading.Thread(target=process_input)
    input_thread.daemon = True
    input_thread.start()
    transaction_thread = threading.Thread(target=end_transaction)
    transaction_thread.daemon = True
    transaction_thread.start()
    try:
        while keepPlaying:
            time.sleep(1)
    except KeyboardInterrupt:
        input_thread.join()
        transaction_thread.join()
        print("Ctrl+C pressed. Exiting...")


if __name__ == "__main__":
    main()
