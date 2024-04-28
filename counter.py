import time
seconds= 0
mints=0
hours=0
with open('seconds.txt', 'w') as file:
    while True:
        
        seconds = seconds+1
        print(seconds,"seconds")
        mints=seconds/60
        hours=mints/60
        print(mints,"minutes")
        print(hours,"Hours")
     
        file.write(f'{seconds}secs\n')
        file.write(f'{mints}mins\n')
        file.write(f'{hours}hrs\n')
        file.write(f'--------------------------------------------------\n')
        
        
        
        file.flush()
        
        time.sleep(1)
        
        
        
        