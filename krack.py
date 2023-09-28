import sms_receive_free

def main():
    # اختر رقم وهمي من مكتبة "sms-receive-free"
    number = "+1234567890"

    # ابدأ حلقة لا نهائية لاستقبال الرسائل
    while True:
        # احصل على قائمة بالرسائل الجديدة
        messages = sms_receive_free.get_messages(number)

        # اطبع معلومات كل رسالة
        for message in messages:
            print("رقم المرسل: " + message["from"])
            print("نص الرسالة: " + message["text"])

        # انتظر ثانية قبل المحاولة مرة أخرى
        time.sleep(1)

if __name__ == "__main__":
    main()
