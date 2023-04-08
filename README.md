# Turing-Machine
A Turing Machine in Python in 30 lines of code
![image](https://user-images.githubusercontent.com/109184310/230700790-a6bdf639-7622-4267-aefd-16de1289b0c2.png)


## On start
On the start of booting the turing machine, you will be placed at position 0 on the metaphorical tape of 1s and 0s. From here you will be prompted with a screen that allows you to enter some input to move along the tape, write to the tape and read the tape. To move along the tape you must type in `>` or `<` to move along. You can layer these, so to move 3 places, you can do `>>>`.<br>

-Note: The turing machine starts you at 0, so make sure you dont type `<` as your first char, otherwise you will get an underflow error.<br>

To read the location on the tape that you are at, you can type in `r`, so to go to the 10th location in memory and read every location on the way, then return back to zero you would type in, `>r>r>r>r>r>r>r>r>r>r<<<<<<<<<<`<br>

Finally to write to a location in memory you would do `w0` or `w1` to write 1 or 0 to memory, so once again to change the first 10 addresses in memory to the binary value `1` it would be `w1>w1>w1>w1>w1>w1>w1>w1>w1>w1<<<<<<<<<<`
