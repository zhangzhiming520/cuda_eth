# cuda_eth
ETH/BNB Mnemonic word collider (ETH/BNB助记词碰撞器)

Local graphics card calculation

NVIDIA 2060：collides 11000+ times per second

Usage steps：

   1）In Password：run mainprint.exe Prompt for password input 
   
   2）Input Core Tread Max：Input the number of cores for calculation, for example, CUDA 2060 is 6000 
   
   3）Cuda chonsenDevice Num：Select the GPU to be calculated 
   
   4) Input start data hex...： How to Calculate, Enter four 32-bit starting numbers for calculation, and then continuously add them up violently.
      
            一) If the second digit of the input is not zero, the calculation will start based on the input data.
      
            二) If the second digit of the input is 333, it will be calculated as a continuously created random number.
      
            三) If the input is 0 0 0 0, create a random number and start accumulating forever.
      
   6) Intermittent Print：How many times to calculate and print once

Dataset file：sethadder.bit
    Run the test dataset，Enter 0 100 0 0 in step 4，The test calculation results will be displayed。

Dataset creation：
        Collect ETH addresses and minimize the letters, such as 0x77478d6c5f821d39c9868e99e231f1ac40a4964c. Due to limited graphics memory on the graphics card, there are too many data sets to fit, so reduce the address size. The rule is as follows: the first 8 bits and last 8 bits of the address remain unchanged: 77478d6c, 40a4964c, and there are 3 8-bit data in the middle. Perform a sum operation, (5f821d39+c9868e99+e231f1ac)&0xfffffff=0B3A 9D7E, then the result is: 77478d6c0b3a9d7e40a4964c, which can refer to the dataset file: sethadder.bit
        
        lg:0x77478d6c5f821d39c9868e99e231f1ac40a4964c
        
           (5f821d39+c9868e99+e231f1ac)&0xfffffff=0b3a9d7e
           
           77478d6c 0b3a9d7e 40a4964c
           
So the NVIDIA 2060 6g can calculate 170 million address data points


Get calculation password: Send 300U to: 0x77478d6c5f821d39c9868e99e231f1ac40a4964c, send transaction information to emil: piao2200@qq.com. If obtaining the source code: 1000U
