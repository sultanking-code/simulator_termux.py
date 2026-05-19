# simulator_termux.py
from rich.console import Console
from rich.table import Table
import random
import time
import csv

console = Console()

class Device:
    def __init__(self, name, platform):
        self.name = name
        self.platform = platform
        self.data_collected = 0
        self.vulnerabilities_found = 0

    def perform_test(self):
        action = random.choice([
            "مسح ملفات النظام الوهمية",
            "محاكاة جمع بيانات",
            "اختبار ثغرة أمنية",
            "محاكاة فتح تطبيق"
        ])
        self.data_collected += random.randint(5, 20)
        self.vulnerabilities_found += random.randint(0, 2)
        return f"{self.name} ({self.platform}) -> {action} | بيانات: {self.data_collected}, ثغرات: {self.vulnerabilities_found}"

    def simulate_payload(self, target):
        payload_result = random.choice([
            "نجاح جزئي في جمع البيانات",
            "تم اكتشاف ثغرة وهمية",
            "لا يوجد استجابة من الهدف",
            "بايلود تم تنفيذه بنجاح وهميًا"
        ])
        self.data_collected += random.randint(5, 15)
        self.vulnerabilities_found += random.randint(0, 3)
        return f"[PAYLOAD] {self.name} -> إرسال بايلود إلى {target} | نتيجة: {payload_result} | بيانات: {self.data_collected}, ثغرات: {self.vulnerabilities_found}"

# الأجهزة
devices = [
    Device("Android افتراضي", "Android"),
    Device("iOS افتراضي", "iOS"),
    Device("جهاز Android الحقيقي", "Android")
]

# وظائف المحاكاة
def run_simulation(rounds=5):
    console.print("[bold red]--- بدء المحاكاة ---[/bold red]")
    for r in range(rounds):
        console.print(f"\n[bold yellow]--- الجولة {r+1} ---[/bold yellow]")
        for dev in devices:
            console.print(dev.perform_test())
            # محاكاة بايلود لكل جهاز
            console.print(dev.simulate_payload("Target_X"))
            time.sleep(0.5)

    console.print("\n[bold green]=== التقارير النهائية ===[/bold green]")
    table = Table(title="تقرير الأجهزة")
    table.add_column("الجهاز", justify="left")
    table.add_column("البيانات المجمعة", justify="right")
    table.add_column("الثغرات المكتشفة", justify="right")
    for dev in devices:
        table.add_row(dev.name, str(dev.data_collected), str(dev.vulnerabilities_found))
    console.print(table)

    # حفظ CSV
    with open("report.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["الجهاز", "البيانات المجمعة", "الثغرات المكتشفة"])
        for dev in devices:
            writer.writerow([dev.name, dev.data_collected, dev.vulnerabilities_found])
    console.print("[bold cyan]تم حفظ التقرير كـ report.csv[/bold cyan]")

if __name__ == "__main__":
    run_simulation()
