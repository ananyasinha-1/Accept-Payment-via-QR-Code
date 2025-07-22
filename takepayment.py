#import qr code generator 
import qrcode
#Input UPI ID from the user
upi_id=input("Enter your upi id: ")

#user se upi pin lena hai as input
phonepay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paypal_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr code for each app
phonepay_qr= qrcode.make(phonepay_url)
google_pay_qr= qrcode.make(google_pay_url)
paytm_qr= qrcode.make(paytm_url)
paypal_qr= qrcode.make(paypal_url)

#save qr code to img file
phonepay_qr.save("phonepay_qr.png")
google_pay_qr.save("google_pay_qr.png")
paytm_qr.save("paytm_qr.png")
paypal_qr.save("paypal_qr.png")

#install PIL/Pillow Library to display qr code
phonepay_qr.show()
google_pay_qr.show()
paytm_qr.show()
paypal_qr.show()