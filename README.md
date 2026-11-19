# Taskflow

## ตั้งค่าระบบสมาชิกและฐานข้อมูล

1. สร้าง Supabase project แล้วคัดลอก PostgreSQL connection string จากหน้า Connect
2. สร้าง OAuth client ใน Google Cloud Console
3. คัดลอก `.streamlit/secrets.toml.example` เป็น `.streamlit/secrets.toml`
4. ใส่ Supabase connection string ใน `[database]` > `url`
5. ใส่ Google Client ID/Secret ใน `[auth.google]` และตั้ง redirect URI ให้ตรงกับ URL ของแอป
6. เปลี่ยน `cookie_secret` เป็นค่าสุ่มที่ยาวและเก็บไฟล์ `secrets.toml` ไว้เป็นความลับ
7. ติดตั้ง dependencies ด้วย `pip install -r requirements.txt` แล้วเริ่มแอปด้วย `streamlit run app.py`

บัญชีสมาชิกใช้รหัส `sub` ที่ยืนยันโดย Google ข้อมูลบัญชี การตั้งค่า และงานจะถูกเก็บแยกตามสมาชิกใน Supabase PostgreSQL โดยบังคับการเชื่อมต่อ TLS ไฟล์ `.streamlit/secrets.toml` มีข้อมูลลับและห้าม commit ขึ้น Git
