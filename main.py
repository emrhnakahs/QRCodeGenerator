import qrcode 
 qr = qrcode.QRCode( 
   version=1, 
   error_correction=qrcode.constants.ERROR_CORRECT_L, 
   box_size=40, #Changes the quality. 
   border=2, #Makes back_color bigger. 
 ) 
 theinput = str(input("Put something: ")) 
 qr.add_data(theinput) 
 img = qr.make_image(fill_color="black", back_color="white") #Fill is qr and the back is the background, you can use transparent too. 
 img.save("qrcode.png") #The input file.
