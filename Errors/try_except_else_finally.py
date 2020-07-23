def ask():
    
    while True:
        try:
            n = int(input('Input a number: '))
        except:
            print('An error occurred. Please try again')
            continue
        else:
            break
        finally:
            print('All done')
                          
     
        
    print('Thank you, The result is: ',n**2)