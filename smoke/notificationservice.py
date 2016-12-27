
def ReadConfiguration():
    #TODO : Read in configuration from conf.txt file
    pass

def SendNotification():
    #TODO add your code here to send an SMS notification out to
    # the phone number in the configuration
    pass

# all of the devices that triggered notifications
def SendSummaryReport():
    #TODO add your code here to send an e-mail report out to
    # the e-mail address in the configuration
    pass

def main():
    ## Display facts about the United States.
    print("Select an option to trigger an event")
    print("1. Send Alert")
    print("2. Send Summary Report")
    print("3. Quit\n")
    while True:
        num = int(input("Make a selection from the menu: "))
        if num == 1:
            SendNotification()
        elif num == 2:
            SendSummaryReport()
        elif num == 3:
            break

main()