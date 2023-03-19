def help1(user=str(input('shiva is  to ready:'))):
    if user=="help":
        print("im ready to locate you:")
        location=input("shall i lock your location(Y/N):")
        if location=="y":
            print("LOCATION LOCKED SUCCESSFULLY:")
        else:
            print("..............OKAY......")
        id1=input("Male or Female:")
        if id1=="female":
            package="medical","police"
            femalename=input("i need your name respected madam:")
            print(femalename)
            print("we can able to provide you this helps:",package)
            femalename1=input("how can i help you madam:")
            if femalename1=="medical":
                medical1="contact near by medical shop ... select 1,"\
                "contact the near by hospital"
                print(medical1)
                medical=input("please select your medical help:")
                if medical=="1"or"select 1":
                    shop1="god medical","contact no:779849809"
                    shop2="life medical","contact no:77908904"
                    shop3="best medical"," oontact no:5095894"
                print("choose the shops do you like to get the help:",shop1,shop2,shop3)
                print("select 1 for shop1")
                print("select 2 for shop2")
                print("select 3 for shop3")
                select=input("these are the availabity you can choose it:")
                if select=="1":
                    shop1name="GOD MEDICAL"
                    print("you have been selected the shop1:",shop1)
                    print("select the your wish.....")
                    print("1.Direction which means map to that location select:1")
                    print("2.contact select:2")
                    print("3.mail select:3")
                    print("4.website select:4")
                    print("5.help select:5")
                    print("6.others select:6")
                    print("7.if you want to put direct order","this OPTION just Enter order")
                    select1=input("choose your option:")
                    if select1=="1":
                        print("you have been selected the MAPS OPTIONS to the",shop1name)
                        print("OPENED MAP")
                    elif select1=="2":
                        print("you have been selected the CONTACTS OPTION of the",shop1name)
                        print("contact")
                        contact=input("shall i contact the ",shop1name,"(Y/N):")
                        if contact=="y":
                            print("Contacting....",shop1name)
                        else:
                            print("contact is here.....")
                    elif select1=="3":
                        print("you have been selected the MAIL OPTION of the",shop1name)
                        print("OPENED MAIL","godmedical@gamil.com")
                    elif select1=="4":
                        print("you have been selected the WEBSITE OPTION of the ",shop1name)
                        print("OPENED", shop1name ,"WEBSITE")
                    elif select1=="5":
                        print("you havee been selected the HELP OPTION")
                        print("Please you can get our help here")
                    elif select1=="6":
                        print("you have been selected OTHERS OPTION")
                        print("others option has been selected ")
                    elif select1=="order":
                        print("you have been selected the ORDER OPTION....")
                        order=input("please enter the name of the medicne")
                        order=input("place order or continue the order(Y/N):")
                        print("..............................................")
                        if order=="y":
                            payment="1.CASH ON DELIVERY",
                            "2.PAYMENT QR CODE",
                            "3.PHONEPE",
                            "4.PHONEPE-WALET",
                            "5.G-PAY(GOOGLE-PAY)",
                            "6.G-PAY WALLET",
                            "7.UPI",
                            "8.NET BANKING",
                            "9.CRIDIT CARD",
                            "10.DEBEIT CARD",
                            "11.BANK"
                            print("..............................................")
                            print(payment)
                            print("CASH ON DELIVERY","select:1")
                            print("PHONEPE","select :2")
                            print("PAYMENT QR CODE","selcet :3")
                            print("PHONEPE-WALLET","select:4")
                            print("G-PAY(GOOLE-PAY)","select:5")
                            print("G-PAY-WALLET","select:6")
                            print("UPI","select:7")
                            print("NET BANKING","select:8")
                            print("CREDIT CARD","select:9")
                            print("DEBEIT CARD","select:10")
                            print("BANK","select:11")
                            print("..............................................")
                            pay=input("please choose choose your  Playment:")
                            if pay=="1":
                                print("you have been select the CASH ON DELIVERY:")
                                adr1=input("please enter your address are delivery point:")
                                adr=''.join(adr1)
                                correction=input("if your address is correct means you can just press(Y/N)")
                                if correction=="y":
                                    print(adr)
                                elif correction=="n":
                                    print("please enter address again:")
                                    print(adr1)
                                    print("...........................")
                                else:
                                    print("please enter your address...")
                                print( femalename,"your order has been placed to.....",adr)
                            elif pay=="2":
                                print("you have been selected the PAYMENT-QR-CODE OPTION.....")
                                print("OPENED PAYMENT-QR-CODE..............")
                                print("SCANNIING..............")
                                upi=input("enter your upiid:")
                                print("............PROCESSING........")
                                print("PAID....................")
                            elif pay=="3":
                                print("selected the PAYMENT QR CODE.............")
                                print("OPENED PHONEPE")
                                print("SCANNING..............")
                            elif pay=="4":
                                print("you have selected the PHONEPE-WALLET")
                                print("OPENED PHONE-WALLET")
                                print("SCANNING...........")
                                p_upi=input("please enter the upi_id:")
                                print("...........PROCCESSING")
                                print("........PAID.......")
                            elif pay=="5":
                                print("you have been selected the GOOGLE-PAY ")
                                print("OPENDED GOOGLE-PAY")
                                print("PROCCESSING.......")
                            elif pay=="6":
                                print("you have been selected the GOOGLE-PAY-WALLET")
                                print("OPENED GOOGEL-PAY-WALLET")
                                print("Enter your upi_id:")
                                print("......PROCCESSING.......")
                                print("................PAID....")
                            elif pay=="7":
                                print("have been selected the UPI:")
                                print("OPENED UIP")
                                upi_upi=input("please enter the upi_id:")
                                print("......PROCESSING")
                                print("..........PAID..")
                            elif pay=="8":
                                print("you have been selected the BANKING")
                                print("BANKING SERVER HAS BEEN OPENED")
                                print("...PROCCESING...")
                                print("PAID")
                            elif pay=="9":
                                print("you have been selected the CREDIT CARD:")
                                print("PROCCESSING TO THE CRIDIT CARD.....")
                                print("......OPENED CARD")
                                crnum=input("please enter credit card number:")
                                print(".........PROCCESING")
                                print(".......PAID........")
                            elif pay=="10":
                                print("you have been selected the DEBEIT CARD")
                                print("PROCCESING TO DEBEIT CARED")
                                print("OPENED DEBEIT CARD ")
                                print("........PAID")
                                denum=input("please enter debeit card:")
                                print("PROCCESSING")
                                print("PAID")
                            elif pay=="11":
                                print("you have been selected the BANK")
                                print("..........OPENED BANK SERVER..")
                                print("...visited bank you can pay ")
                                print("..........PAID")
                elif select=="2":
                    shop2name="LIFE MEDICAL"
                    print("you have been selected the shop1:",shop2name)
                    print("select the your wish.....")
                    print("1.Direction which means map to that location select:1")
                    print("2.contact select:2")
                    print("3.mail select:3")
                    print("4.website select:4")
                    print("5.help select:5")
                    print("6.others select:6")
                    print("7.if you want to put direct order","this OPTION just Enter order")
                    select1=input("choose your option:")
                    if select1=="1":
                        print("you have been selected the MAPS OPTIONS to the",shop1name)
                        print("OPENED MAP")
                    elif select1=="2":
                        print("you have been selected the CONTACTS OPTION of the",shop1name)
                        print("contact")
                        contact=input("shall i contact the ",shop2name,"(Y/N):")
                        if contact=="y":
                            print("Contacting....",shop2name)
                        else:
                            print("contact is here.....")
                    elif select1=="3":
                        print("you have been selected the MAIL OPTION of the",shop2name)
                        print("OPENED MAIL","godmedical@gamil.com")
                    elif select1=="4":
                        print("you have been selected the WEBSITE OPTION of the ",shop2name)
                        print("OPENED", shop2name ,"WEBSITE")
                    elif select1=="5":
                        print("you havee been selected the HELP OPTION")
                        print("Please you can get our help here")
                    elif select1=="6":
                        print("you have been selected OTHERS OPTION")
                        print("others option has been selected ")
                    elif select1=="order":
                        print("you have been selected the ORDER OPTION....")
                        order=input("please enter the name of the medicne")
                        order=input("place order or continue the order(Y/N):")
                        print("..............................................")
                        if order=="y":
                            payment="1.CASH ON DELIVERY",
                            "2.PAYMENT QR CODE",
                            "3.PHONEPE",
                            "4.PHONEPE-WALET",
                            "5.G-PAY(GOOGLE-PAY)",
                            "6.G-PAY WALLET",
                            "7.UPI",
                            "8.NET BANKING",
                            "9.CRIDIT CARD",
                            "10.DEBEIT CARD",
                            "11.BANK"
                            print("..............................................")
                            print(payment)
                            print("CASH ON DELIVERY","select:1")
                            print("PHONEPE","select :2")
                            print("PAYMENT QR CODE","selcet :3")
                            print("PHONEPE-WALLET","select:4")
                            print("G-PAY(GOOLE-PAY)","select:5")
                            print("G-PAY-WALLET","select:6")
                            print("UPI","select:7")
                            print("NET BANKING","select:8")
                            print("CREDIT CARD","select:9")
                            print("DEBEIT CARD","select:10")
                            print("BANK","select:11")
                            print("..............................................")
                            pay=input("please choose choose your  Playment:")
                            if pay=="1":
                                print("you have been select the CASH ON DELIVERY:")
                                adr1=input("please enter your address are delivery point:")
                                adr=''.join(adr1)
                                correction=input("if your address is correct means you can just press(Y/N)")
                                if correction=="y":
                                    print(adr)
                                elif correction=="n":
                                    print("please enter address again:")
                                    print(adr1)
                                    print("...........................")
                                else:
                                    print("please enter your address...")
                                print( femalename,"your order has been placed to.....",adr)
                            elif pay=="2":
                                print("you have been selected the PAYMENT-QR-CODE OPTION.....")
                                print("OPENED PAYMENT-QR-CODE..............")
                                print("SCANNIING..............")
                                upi=input("enter your upiid:")
                                print("............PROCESSING........")
                                print("PAID....................")
                            elif pay=="3":
                                print("selected the PAYMENT QR CODE.............")
                                print("OPENED PHONEPE")
                                print("SCANNING..............")
                            elif pay=="4":
                                print("you have selected the PHONEPE-WALLET")
                                print("OPENED PHONE-WALLET")
                                print("SCANNING...........")
                                p_upi=input("please enter the upi_id:")
                                print("...........PROCCESSING")
                                print("........PAID.......")
                            elif pay=="5":
                                print("you have been selected the GOOGLE-PAY ")
                                print("OPENDED GOOGLE-PAY")
                                print("PROCCESSING.......")
                            elif pay=="6":
                                print("you have been selected the GOOGLE-PAY-WALLET")
                                print("OPENED GOOGEL-PAY-WALLET")
                                print("Enter your upi_id:")
                                print("......PROCCESSING.......")
                                print("................PAID....")
                            elif pay=="7":
                                print("have been selected the UPI:")
                                print("OPENED UIP")
                                upi_upi=input("please enter the upi_id:")
                                print("......PROCESSING")
                                print("..........PAID..")
                            elif pay=="8":
                                print("you have been selected the BANKING")
                                print("BANKING SERVER HAS BEEN OPENED")
                                print("...PROCCESING...")
                                print("PAID")
                            elif pay=="9":
                                print("you have been selected the CREDIT CARD:")
                                print("PROCCESSING TO THE CRIDIT CARD.....")
                                print("......OPENED CARD")
                                crnum=input("please enter credit card number:")
                                print(".........PROCCESING")
                                print(".......PAID........")
                            elif pay=="10":
                                print("you have been selected the DEBEIT CARD")
                                print("PROCCESING TO DEBEIT CARED")
                                print("OPENED DEBEIT CARD ")
                                print("........PAID")
                                denum=input("please enter debeit card:")
                                print("PROCCESSING")
                                print("PAID")
                            elif pay=="11":
                                print("you have been selected the BANK")
                                print("..........OPENED BANK SERVER..")
                                print("...visited bank you can pay ")
                                print("..........PAID")
                                    
                elif select=="3":
                    shop3name="BEST MEDICAL"
                    print("you have been selected the shop1:",shop3name)
                    print("select the your wish.....")
                    print("1.Direction which means map to that location select:1")
                    print("2.contact select:2")
                    print("3.mail select:3")
                    print("4.website select:4")
                    print("5.help select:5")
                    print("6.others select:6")
                    print("7.if you want to put direct order","this OPTION just Enter order")
                    select1=input("choose your option:")
                    if select1=="1":
                        print("you have been selected the MAPS OPTIONS to the",shop3name)
                        print("OPENED MAP")
                    elif select1=="2":
                        print("you have been selected the CONTACTS OPTION of the",shop3name)
                        print("contact")
                        contact=input("shall i contact the ",shop3name,"(Y/N):")
                        if contact=="y":
                            print("Contacting....",shop3name)
                        else:
                            print("contact is here.....")
                    elif select1=="3":
                        print("you have been selected the MAIL OPTION of the",shop3name)
                        print("OPENED MAIL","godmedical@gamil.com")
                    elif select1=="4":
                        print("you have been selected the WEBSITE OPTION of the ",shop3name)
                        print("OPENED", shop3name ,"WEBSITE")
                    elif select1=="5":
                        print("you havee been selected the HELP OPTION")
                        print("Please you can get our help here")
                    elif select1=="6":
                        print("you have been selected OTHERS OPTION")
                        print("others option has been selected ")
                    elif select1=="order": 
                        print("you have been selected the ORDER OPTION....")
                        order=input("please enter the name of the medicne")
                        order=input("place order or continue the order(Y/N):")
                        print("..............................................")
                        if order=="y":
                            payment="1.CASH ON DELIVERY",
                            "2.PAYMENT QR CODE",
                            "3.PHONEPE",
                            "4.PHONEPE-WALET",
                            "5.G-PAY(GOOGLE-PAY)",
                            "6.G-PAY WALLET",
                            "7.UPI",
                            "8.NET BANKING",
                            "9.CRIDIT CARD",
                            "10.DEBEIT CARD",
                            "11.BANK"
                            print("..............................................")
                            print(payment)
                            print("CASH ON DELIVERY","select:1")
                            print("PHONEPE","select :2")
                            print("PAYMENT QR CODE","selcet :3")
                            print("PHONEPE-WALLET","select:4")
                            print("G-PAY(GOOLE-PAY)","select:5")
                            print("G-PAY-WALLET","select:6")
                            print("UPI","select:7")
                            print("NET BANKING","select:8")
                            print("CREDIT CARD","select:9")
                            print("DEBEIT CARD","select:10")
                            print("BANK","select:11")
                            print("..............................................")
                            pay=input("please choose choose your  Playment:")
                            if pay=="1":
                                print("you have been select the CASH ON DELIVERY:")
                                adr1=input("please enter your address are delivery point:")
                                adr=''.join(adr1)
                                correction=input("if your address is correct means you can just press(Y/N)")
                                if correction=="y":
                                    print(adr)
                                elif correction=="n":
                                    print("please enter address again:")
                                    print(adr1)
                                    print("...........................")
                                else:
                                    print("please enter your address...")
                                print( femalename,"your order has been placed to.....",adr)
                            elif pay=="2":
                                print("you have been selected the PAYMENT-QR-CODE OPTION.....")
                                print("OPENED PAYMENT-QR-CODE..............")
                                print("SCANNIING..............")
                                upi=input("enter your upiid:")
                                print("............PROCESSING........")
                                print("PAID....................")
                            elif pay=="3":
                                print("selected the PAYMENT QR CODE.............")
                                print("OPENED PHONEPE")
                                print("SCANNING..............")
                            elif pay=="4":
                                print("you have selected the PHONEPE-WALLET")
                                print("OPENED PHONE-WALLET")
                                print("SCANNING...........")
                                p_upi=input("please enter the upi_id:")
                                print("...........PROCCESSING")
                                print("........PAID.......")
                            elif pay=="5":
                                print("you have been selected the GOOGLE-PAY ")
                                print("OPENDED GOOGLE-PAY")
                                print("PROCCESSING.......")
                            elif pay=="6":
                                print("you have been selected the GOOGLE-PAY-WALLET")
                                print("OPENED GOOGEL-PAY-WALLET")
                                print("Enter your upi_id:")
                                print("......PROCCESSING.......")
                                print("................PAID....")
                            elif pay=="7":
                                print("have been selected the UPI:")
                                print("OPENED UIP")
                                upi_upi=input("please enter the upi_id:")
                                print("......PROCESSING")
                                print("..........PAID..")
                            elif pay=="8":
                                print("you have been selected the BANKING")
                                print("BANKING SERVER HAS BEEN OPENED")
                                print("...PROCCESING...")
                                print("PAID")
                            elif pay=="9":
                                print("you have been selected the CREDIT CARD:")
                                print("PROCCESSING TO THE CRIDIT CARD.....")
                                print("......OPENED CARD")
                                crnum=input("please enter credit card number:")
                                print(".........PROCCESING")
                                print(".......PAID........")
                            elif pay=="10":
                                print("you have been selected the DEBEIT CARD")
                                print("PROCCESING TO DEBEIT CARED")
                                print("OPENED DEBEIT CARD ")
                                print("........PAID")
                                denum=input("please enter debeit card:")
                                print("PROCCESSING")
                                print("PAID")
                            elif pay=="11":
                                print("you have been selected the BANK")
                                print("..........OPENED BANK SERVER..")
                                print("...visited bank you can pay ")
                                print("..........PAID")
        elif id1=="male":
           package="medical","police"
           malename=input("i need your name respected sir:")
           print(malename,"how can i help sir")
           print("we can able to provide you this helps:",package)
           femalename1=input("how can i help you sir:")
           if femalename1=="medical":
                medical1="contact near by medical shop ... select 1,"\
                "contact the near by hospital"
                print(medical1)
                medical=input("please select your medical help:")
                if medical=="1"or"select 1":
                    shop1="god medical","contact no:779849809"
                    shop2="life medical","contact no:77908904"
                    shop3="best medical"," oontact no:5095894"
                print("choose the shops do you like to get the help:",shop1,shop2,shop3)
                print("select 1 for shop1")
                print("select 2 for shop2")
                print("select 3 for shop3")
                select=input("these are the availabity you can choose it:")
                if select=="1":
                    shop1name="GOD MEDICAL"
                    print("you have been selected the shop1:",shop1)
                    print("select the your wish.....")
                    print("1.Direction which means map to that location select:1")
                    print("2.contact select:2")
                    print("3.mail select:3")
                    print("4.website select:4")
                    print("5.help select:5")
                    print("6.others select:6")
                    print("7.if you want to put direct order","this OPTION just Enter order")
                    select1=input("choose your option:")
                    if select1=="1":
                        print("you have been selected the MAPS OPTIONS to the",shop1name)
                        print("OPENED MAP")
                    elif select1=="2":
                        print("you have been selected the CONTACTS OPTION of the",shop1name)
                        print("contact")
                        contact=input("shall i contact the ",shop1name,"(Y/N):")
                        if contact=="y":
                            print("Contacting....",shop1name)
                        else:
                            print("contact is here.....")
                    elif select1=="3":
                        print("you have been selected the MAIL OPTION of the",shop1name)
                        print("OPENED MAIL","godmedical@gamil.com")
                    elif select1=="4":
                        print("you have been selected the WEBSITE OPTION of the ",shop1name)
                        print("OPENED", shop1name ,"WEBSITE")
                    elif select1=="5":
                        print("you havee been selected the HELP OPTION")
                        print("Please you can get our help here")
                    elif select1=="6":
                        print("you have been selected OTHERS OPTION")
                        print("others option has been selected ")
                    elif select1=="order":
                        print("you have been selected the ORDER OPTION....")
                        order=input("please enter the name of the medicne")
                        order=input("place order or continue the order(Y/N):")
                        print("..............................................")
                        if order=="y":
                            payment="1.CASH ON DELIVERY",
                            "2.PAYMENT QR CODE",
                            "3.PHONEPE",
                            "4.PHONEPE-WALET",
                            "5.G-PAY(GOOGLE-PAY)",
                            "6.G-PAY WALLET",
                            "7.UPI",
                            "8.NET BANKING",
                            "9.CRIDIT CARD",
                            "10.DEBEIT CARD",
                            "11.BANK"
                            print("..............................................")
                            print(payment)
                            print("CASH ON DELIVERY","select:1")
                            print("PHONEPE","select :2")
                            print("PAYMENT QR CODE","selcet :3")
                            print("PHONEPE-WALLET","select:4")
                            print("G-PAY(GOOLE-PAY)","select:5")
                            print("G-PAY-WALLET","select:6")
                            print("UPI","select:7")
                            print("NET BANKING","select:8")
                            print("CREDIT CARD","select:9")
                            print("DEBEIT CARD","select:10")
                            print("BANK","select:11")
                            print("..............................................")
                            pay=input("please choose choose your  Playment:")
                            if pay=="1":
                                print("you have been select the CASH ON DELIVERY:")
                                adr1=input("please enter your address are delivery point:")
                                adr=''.join(adr1)
                                correction=input("if your address is correct means you can just press(Y/N)")
                                if correction=="y":
                                    print(adr)
                                elif correction=="n":
                                    print("please enter address again:")
                                    print(adr1)
                                    print("...........................")
                                else:
                                    print("please enter your address...")
                                print(malename,"your order has been placed to.....",adr)
                            elif pay=="2":
                                print("you have been selected the PAYMENT-QR-CODE OPTION.....")
                                print("OPENED PAYMENT-QR-CODE..............")
                                print("SCANNIING..............")
                                upi=input("enter your upiid:")
                                print("............PROCESSING........")
                                print("PAID....................")
                            elif pay=="3":
                                print("selected the PAYMENT QR CODE.............")
                                print("OPENED PHONEPE")
                                print("SCANNING..............")
                            elif pay=="4":
                                print("you have selected the PHONEPE-WALLET")
                                print("OPENED PHONE-WALLET")
                                print("SCANNING...........")
                                p_upi=input("please enter the upi_id:")
                                print("...........PROCCESSING")
                                print("........PAID.......")
                            elif pay=="5":
                                print("you have been selected the GOOGLE-PAY ")
                                print("OPENDED GOOGLE-PAY")
                                print("PROCCESSING.......")
                            elif pay=="6":
                                print("you have been selected the GOOGLE-PAY-WALLET")
                                print("OPENED GOOGEL-PAY-WALLET")
                                print("Enter your upi_id:")
                                print("......PROCCESSING.......")
                                print("................PAID....")
                            elif pay=="7":
                                print("have been selected the UPI:")
                                print("OPENED UIP")
                                upi_upi=input("please enter the upi_id:")
                                print("......PROCESSING")
                                print("..........PAID..")
                            elif pay=="8":
                                print("you have been selected the BANKING")
                                print("BANKING SERVER HAS BEEN OPENED")
                                print("...PROCCESING...")
                                print("PAID")
                            elif pay=="9":
                                print("you have been selected the CREDIT CARD:")
                                print("PROCCESSING TO THE CRIDIT CARD.....")
                                print("......OPENED CARD")
                                crnum=input("please enter credit card number:")
                                print(".........PROCCESING")
                                print(".......PAID........")
                            elif pay=="10":
                                print("you have been selected the DEBEIT CARD")
                                print("PROCCESING TO DEBEIT CARED")
                                print("OPENED DEBEIT CARD ")
                                print("........PAID")
                                denum=input("please enter debeit card:")
                                print("PROCCESSING")
                                print("PAID")
                            elif pay=="11":
                                print("you have been selected the BANK")
                                print("..........OPENED BANK SERVER..")
                                print("...visited bank you can pay ")
                                print("..........PAID")
                elif select=="2":
                    shop2name="LIFE MEDICAL"
                    print("you have been selected the shop1:",shop2name)
                    print("select the your wish.....")
                    print("1.Direction which means map to that location select:1")
                    print("2.contact select:2")
                    print("3.mail select:3")
                    print("4.website select:4")
                    print("5.help select:5")
                    print("6.others select:6")
                    print("7.if you want to put direct order","this OPTION just Enter order")
                    select1=input("choose your option:")
                    if select1=="1":
                        print("you have been selected the MAPS OPTIONS to the",shop1name)
                        print("OPENED MAP")
                    elif select1=="2":
                        print("you have been selected the CONTACTS OPTION of the",shop1name)
                        print("contact")
                        contact=input("shall i contact the ",shop2name,"(Y/N):")
                        if contact=="y":
                            print("Contacting....",shop2name)
                        else:
                            print("contact is here.....")
                    elif select1=="3":
                        print("you have been selected the MAIL OPTION of the",shop2name)
                        print("OPENED MAIL","godmedical@gamil.com")
                    elif select1=="4":
                        print("you have been selected the WEBSITE OPTION of the ",shop2name)
                        print("OPENED", shop2name ,"WEBSITE")
                    elif select1=="5":
                        print("you havee been selected the HELP OPTION")
                        print("Please you can get our help here")
                    elif select1=="6":
                        print("you have been selected OTHERS OPTION")
                        print("others option has been selected ")
                    elif select1=="order":
                        print("you have been selected the ORDER OPTION....")
                        order=input("please enter the name of the medicne")
                        order=input("place order or continue the order(Y/N):")
                        print("..............................................")
                        if order=="y":
                            payment="1.CASH ON DELIVERY",
                            "2.PAYMENT QR CODE",
                            "3.PHONEPE",
                            "4.PHONEPE-WALET",
                            "5.G-PAY(GOOGLE-PAY)",
                            "6.G-PAY WALLET",
                            "7.UPI",
                            "8.NET BANKING",
                            "9.CRIDIT CARD",
                            "10.DEBEIT CARD",
                            "11.BANK"
                            print("..............................................")
                            print(payment)
                            print("CASH ON DELIVERY","select:1")
                            print("PHONEPE","select :2")
                            print("PAYMENT QR CODE","selcet :3")
                            print("PHONEPE-WALLET","select:4")
                            print("G-PAY(GOOLE-PAY)","select:5")
                            print("G-PAY-WALLET","select:6")
                            print("UPI","select:7")
                            print("NET BANKING","select:8")
                            print("CREDIT CARD","select:9")
                            print("DEBEIT CARD","select:10")
                            print("BANK","select:11")
                            print("..............................................")
                            pay=input("please choose choose your  Playment:")
                            if pay=="1":
                                print("you have been select the CASH ON DELIVERY:")
                                adr1=input("please enter your address are delivery point:")
                                adr=''.join(adr1)
                                correction=input("if your address is correct means you can just press(Y/N)")
                                if correction=="y":
                                    print(adr)
                                elif correction=="n":
                                    print("please enter address again:")
                                    print(adr1)
                                    print("...........................")
                                else:
                                    print("please enter your address...")
                                print(malename,"your order has been placed to.....",adr)
                            elif pay=="2":
                                print("you have been selected the PAYMENT-QR-CODE OPTION.....")
                                print("OPENED PAYMENT-QR-CODE..............")
                                print("SCANNIING..............")
                                upi=input("enter your upiid:")
                                print("............PROCESSING........")
                                print("PAID....................")
                            elif pay=="3":
                                print("selected the PAYMENT QR CODE.............")
                                print("OPENED PHONEPE")
                                print("SCANNING..............")
                            elif pay=="4":
                                print("you have selected the PHONEPE-WALLET")
                                print("OPENED PHONE-WALLET")
                                print("SCANNING...........")
                                p_upi=input("please enter the upi_id:")
                                print("...........PROCCESSING")
                                print("........PAID.......")
                            elif pay=="5":
                                print("you have been selected the GOOGLE-PAY ")
                                print("OPENDED GOOGLE-PAY")
                                print("PROCCESSING.......")
                            elif pay=="6":
                                print("you have been selected the GOOGLE-PAY-WALLET")
                                print("OPENED GOOGEL-PAY-WALLET")
                                print("Enter your upi_id:")
                                print("......PROCCESSING.......")
                                print("................PAID....")
                            elif pay=="7":
                                print("have been selected the UPI:")
                                print("OPENED UIP")
                                upi_upi=input("please enter the upi_id:")
                                print("......PROCESSING")
                                print("..........PAID..")
                            elif pay=="8":
                                print("you have been selected the BANKING")
                                print("BANKING SERVER HAS BEEN OPENED")
                                print("...PROCCESING...")
                                print("PAID")
                            elif pay=="9":
                                print("you have been selected the CREDIT CARD:")
                                print("PROCCESSING TO THE CRIDIT CARD.....")
                                print("......OPENED CARD")
                                crnum=input("please enter credit card number:")
                                print(".........PROCCESING")
                                print(".......PAID........")
                            elif pay=="10":
                                print("you have been selected the DEBEIT CARD")
                                print("PROCCESING TO DEBEIT CARED")
                                print("OPENED DEBEIT CARD ")
                                print("........PAID")
                                denum=input("please enter debeit card:")
                                print("PROCCESSING")
                                print("PAID")
                            elif pay=="11":
                                print("you have been selected the BANK")
                                print("..........OPENED BANK SERVER..")
                                print("...visited bank you can pay ")
                                print("..........PAID")
                                    
                elif select=="3":
                    shop3name="BEST MEDICAL"
                    print("you have been selected the shop1:",shop3name)
                    print("select the your wish.....")
                    print("1.Direction which means map to that location select:1")
                    print("2.contact select:2")
                    print("3.mail select:3")
                    print("4.website select:4")
                    print("5.help select:5")
                    print("6.others select:6")
                    print("7.if you want to put direct order","this OPTION just Enter order")
                    select1=input("choose your option:")
                    if select1=="1":
                        print("you have been selected the MAPS OPTIONS to the",shop3name)
                        print("OPENED MAP")
                    elif select1=="2":
                        print("you have been selected the CONTACTS OPTION of the",shop3name)
                        print("contact")
                        contact=input("shall i contact the ",shop3name,"(Y/N):")
                        if contact=="y":
                            print("Contacting....",shop3name)
                        else:
                            print("contact is here.....")
                    elif select1=="3":
                        print("you have been selected the MAIL OPTION of the",shop3name)
                        print("OPENED MAIL","godmedical@gamil.com")
                    elif select1=="4":
                        print("you have been selected the WEBSITE OPTION of the ",shop3name)
                        print("OPENED", shop3name ,"WEBSITE")
                    elif select1=="5":
                        print("you havee been selected the HELP OPTION")
                        print("Please you can get our help here")
                    elif select1=="6":
                        print("you have been selected OTHERS OPTION")
                        print("others option has been selected ")
                    elif select1=="order": 
                        print("you have been selected the ORDER OPTION....")
                        order=input("please enter the name of the medicne")
                        order=input("place order or continue the order(Y/N):")
                        print("..............................................")
                        if order=="y":
                            payment="1.CASH ON DELIVERY",
                            "2.PAYMENT QR CODE",
                            "3.PHONEPE",
                            "4.PHONEPE-WALET",
                            "5.G-PAY(GOOGLE-PAY)",
                            "6.G-PAY WALLET",
                            "7.UPI",
                            "8.NET BANKING",
                            "9.CRIDIT CARD",
                            "10.DEBEIT CARD",
                            "11.BANK"
                            print("..............................................")
                            print(payment)
                            print("CASH ON DELIVERY","select:1")
                            print("PHONEPE","select :2")
                            print("PAYMENT QR CODE","selcet :3")
                            print("PHONEPE-WALLET","select:4")
                            print("G-PAY(GOOLE-PAY)","select:5")
                            print("G-PAY-WALLET","select:6")
                            print("UPI","select:7")
                            print("NET BANKING","select:8")
                            print("CREDIT CARD","select:9")
                            print("DEBEIT CARD","select:10")
                            print("BANK","select:11")
                            print("..............................................")
                            pay=input("please choose choose your  Playment:")
                            if pay=="1":
                                print("you have been select the CASH ON DELIVERY:")
                                adr1=input("please enter your address are delivery point:")
                                adr=''.join(adr1)
                                correction=input("if your address is correct means you can just press(Y/N)")
                                if correction=="y":
                                    print(adr)
                                elif correction=="n":
                                    print("please enter address again:")
                                    print(adr1)
                                    print("...........................")
                                else:
                                    print("please enter your address...")
                                print(malename,"your order has been placed to.....",adr)
                            elif pay=="2":
                                print("you have been selected the PAYMENT-QR-CODE OPTION.....")
                                print("OPENED PAYMENT-QR-CODE..............")
                                print("SCANNIING..............")
                                upi=input("enter your upiid:")
                                print("............PROCESSING........")
                                print("PAID....................")
                            elif pay=="3":
                                print("selected the PAYMENT QR CODE.............")
                                print("OPENED PHONEPE")
                                print("SCANNING..............")
                            elif pay=="4":
                                print("you have selected the PHONEPE-WALLET")
                                print("OPENED PHONE-WALLET")
                                print("SCANNING...........")
                                p_upi=input("please enter the upi_id:")
                                print("...........PROCCESSING")
                                print("........PAID.......")
                            elif pay=="5":
                                print("you have been selected the GOOGLE-PAY ")
                                print("OPENDED GOOGLE-PAY")
                                print("PROCCESSING.......")
                            elif pay=="6":
                                print("you have been selected the GOOGLE-PAY-WALLET")
                                print("OPENED GOOGEL-PAY-WALLET")
                                print("Enter your upi_id:")
                                print("......PROCCESSING.......")
                                print("................PAID....")
                            elif pay=="7":
                                print("have been selected the UPI:")
                                print("OPENED UIP")
                                upi_upi=input("please enter the upi_id:")
                                print("......PROCESSING")
                                print("..........PAID..")
                            elif pay=="8":
                                print("you have been selected the BANKING")
                                print("BANKING SERVER HAS BEEN OPENED")
                                print("...PROCCESING...")
                                print("PAID")
                            elif pay=="9":
                                print("you have been selected the CREDIT CARD:")
                                print("PROCCESSING TO THE CRIDIT CARD.....")
                                print("......OPENED CARD")
                                crnum=input("please enter credit card number:")
                                print(".........PROCCESING")
                                print(".......PAID........")
                            elif pay=="10":
                                print("you have been selected the DEBEIT CARD")
                                print("PROCCESING TO DEBEIT CARED")
                                print("OPENED DEBEIT CARD ")
                                print("........PAID")
                                denum=input("please enter debeit card:")
                                print("PROCCESSING")
                                print("PAID")
                            elif pay=="11":
                                print("you have been selected the BANK")
                                print("..........OPENED BANK SERVER..")
                                print("...visited bank you can pay ")
                                print("..........PAID")                          
help1()
