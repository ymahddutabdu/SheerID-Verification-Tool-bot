# services/googleone_check.py
import sys
import os
import subprocess

def verify_googleone(url):
    try:
        # استدعاء سكربت التحقق من مجلد one-verify-tool وتمرير الرابط
        result = subprocess.check_output(
            ["python", "one-verify-tool/main.py", url],  # غيّر اسم الملف حسب الموجود عندك
            cwd=os.path.dirname(os.path.dirname(__file__))  # يرجع للمسار الرئيسي للمشروع
        )
        return result.decode("utf-8")
    except Exception as e:
        return f"خطأ أثناء التحقق: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        print(verify_googleone(url))
    else:
        print("لم يتم تمرير رابط للتحقق")
