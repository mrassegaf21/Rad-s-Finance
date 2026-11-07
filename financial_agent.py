import datetime
import json
import os

class FinancialAgent:
    def __init__(self, monthly_budget, filename="financial_data.json"):
        """Inisialisasi Agen dengan Budget Bulanan dan Penyimpanan File"""
        self.monthly_budget = monthly_budget
        self.filename = filename
        self.expenses = []  # Memori internal agen
        self.load_data()

    def load_data(self):
        """Modul Memori Jangka Panjang: Memuat data dari file JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.expenses = json.load(file)
            except Exception:
                self.expenses = []

    def save_data(self):
        """Modul Penyimpanan Otomatis ke File JSON"""
        try:
            with open(self.filename, "w") as file:
                json.dump(self.expenses, file, indent=4)
        except Exception as e:
            print(f"Gagal menyimpan data: {e}")

    def add_expense(self, amount, category, note):
        """Modul Pencatatan Pengeluaran & Utility-Based Logic"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        transaction = {
            "time": timestamp,
            "amount": amount,
            "category": category,
            "note": note
        }
        self.expenses.append(transaction)
        self.save_data()
        
        total_spent = sum(item["amount"] for item in self.expenses)
        spent_percentage = (total_spent / self.monthly_budget) * 100
        
        # Evaluasi utilitas / kondisi keuangan (Utility-Based Decision)
        if total_spent > self.monthly_budget:
            status_msg = "\033[91m🚨 PERINGATAN KRITIS: Pengeluaran melampaui batas budget!\033[0m"
        elif spent_percentage >= 80:
            status_msg = f"\033[93m⚠️ PERINGATAN: Pengeluaran sudah mencapai {spent_percentage:.1f}%!\033[0m"
        else:
            status_msg = f"\033[92m✅ Status Keuangan: Aman ({spent_percentage:.1f}% terpakai)\033[0m"

        result = f"""
\033[96m+----------------------------------------+\033[0m
\033[92m|      TRANSAKSI BERHASIL DICATAT        |\033[0m
\033[96m+----------------------------------------+\033[0m
 Waktu    : {timestamp}
 Kategori : {category.upper()} ({note})
 Nominal  : Rp{amount:,}
------------------------------------------
 Total Keluar : Rp{total_spent:,}
 Sisa Budget  : Rp{max(0, self.monthly_budget - total_spent):,}
 {status_msg}
\033[96m+----------------------------------------+\033[0m
"""
        return result

    def evaluate_finances(self):
        """Modul Financial Advisor / Pemberi Saran Otomatis"""
        if not self.expenses:
            return "\033[93mBelum ada transaksi yang tercatat bulan ini.\033[0m"

        total_spent = sum(item["amount"] for item in self.expenses)
        remaining = self.monthly_budget - total_spent
        spent_percentage = (total_spent / self.monthly_budget) * 100

        # Menganalisis kategori pengeluaran terbesar
        categories = {}
        for item in self.expenses:
            cat = item["category"]
            categories[cat] = categories.get(cat, 0) + item["amount"]
        
        largest_cat = max(categories, key=categories.get) if categories else "Umum"

        # Aturan Saran (Rule-Based Expert Logic)
        if spent_percentage > 85:
            advice = f"Segera rem pengeluaran! Terbesar di '{largest_cat}'. Hindari belanja non-esensial."
        elif spent_percentage > 50:
            advice = f"Kondisi stabil, namun waspadai kategori '{largest_cat}' yang menyerap porsi besar."
        else:
            advice = "Keuangan sangat sehat! Pertahankan pola ini dan sisihkan untuk tabungan."

        report = f"""
\033[95m==========================================\033[0m
\033[1m          LAPORAN & ANALISIS AGEN         \033[0m
\033[95m==========================================\033[0m
 Total Budget  : Rp{self.monthly_budget:,}
 Total Keluar  : Rp{total_spent:,}
 Sisa Anggaran : Rp{remaining:,}
 Pengeluaran Tertinggi: {largest_cat.upper()} (Rp{categories[largest_cat]:,})
------------------------------------------
 \033[96m[Analisis AI Agent]:\033[0m 
 {advice}
\033[95m==========================================\033[0m
"""
        return report

    def show_history(self):
        """Modul Menampilkan Riwayat Transaksi"""
        if not self.expenses:
            return "\033[93mBelum ada riwayat transaksi.\033[0m"
        
        history_str = "\n\033[94m================ RIWAYAT TRANSAKSI ================\033[0m\n"
        for idx, item in enumerate(self.expenses, 1):
            history_str += f" {idx}. [{item['time']}] \033[1m{item['category'].upper()}\033[0m - Rp{item['amount']:,} *({item['note']})*\n"
        history_str += "\033[94m===================================================\033[0m"
        return history_str


# --- PROGRAM UTAMA (DENGAN TAMPILAN DASHBOARD) ---
if __name__ == "__main__":
    my_agent = FinancialAgent(monthly_budget=1500000)
    
    while True:
        # Hitung statistik cepat untuk header dashboard
        total_spent = sum(item["amount"] for item in my_agent.expenses)
        remaining = my_agent.monthly_budget - total_spent
        
        print("\n" + "="*50)
        print("\033[96m 🤖 AI FINANCIAL ASSISTANT AGENT (DASHBOARD)\033[0m")
        print("="*50)
        print(f" 💰 Budget: Rp{my_agent.monthly_budget:,} | Terpakai: Rp{total_spent:,} | Sisa: Rp{remaining:,}")
        print("-"*50)
        print(" [1] ➕ Tambah Pengeluaran")
        print(" [2] 📊 Cek Laporan & Analisis AI")
        print(" [3] 📜 Lihat Riwayat Transaksi")
        print(" [4] ❌ Keluar")
        print("="*50)
        
        pilih = input(" 👉 Masukkan pilihan menu (1-4): ").strip()
        
        if pilih == "4" or pilih.lower() == "keluar":
            print("\n\033[92m Terima kasih telah menggunakan AI Financial Agent! Sampai jumpa.\033[0m\n")
            break
        elif pilih == "1" or pilih.lower() == "tambah":
            try:
                print("\n--- Form Input Transaksi Baru ---")
                amt = int(input(" Masukkan jumlah nominal (contoh: 50000): "))
                cat = input(" Masukkan kategori (contoh: Makanan, Transport, Hiburan): ")
                nt = input(" Catatan singkat (contoh: Makan malam): ")
                print(my_agent.add_expense(amt, cat, nt))
            except ValueError:
                print("\n\033[91m❌ Error: Nominal harus berupa angka yang valid!\033[0m")
        elif pilih == "2" or pilih.lower() == "cek":
            print(my_agent.evaluate_finances())
        elif pilih == "3" or pilih.lower() == "riwayat":
            print(my_agent.show_history())
        else:
            print("\n\033[91m❌ Pilihan tidak valid. Silakan masukkan angka 1 sampai 4.\033[0m")