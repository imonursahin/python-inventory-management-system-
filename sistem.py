import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3


#Veritabnı İşlemleri

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("stok.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS stoklar (id PRIMARYKEY text, s_ad text, s_grup text, s_birim text, a_tarih text, a_fiyat text, s_fiyat text, sg_miktar text, m_miktar text, t_ad text, t_iletisim text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, id, s_ad, s_grup, s_birim, a_tarih, a_fiyat, s_fiyat, sg_miktar, m_miktar, t_ad, t_iletisim):
        self.dbCursor.execute("INSERT INTO stoklar VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, s_ad, s_grup, s_birim, a_tarih, a_fiyat, s_fiyat, sg_miktar, m_miktar, t_ad, t_iletisim))
        self.dbConnection.commit()
        
    def Update(self, s_ad, s_grup, s_birim, a_tarih, a_fiyat, s_fiyat, sg_miktar, m_miktar, t_ad, t_iletisim, id):
        self.dbCursor.execute("UPDATE stoklar SET s_ad = ?, s_grup = ?, s_birim = ?, a_tarih = ?, a_fiyat = ?, s_fiyat = ?, sg_miktar = ?, m_miktar = ?, t_ad = ?, t_iletisim = ? WHERE id = ?", (s_ad, s_grup, s_birim, a_tarih, a_fiyat, s_fiyat, sg_miktar, m_miktar, t_ad, t_iletisim, id))
        self.dbConnection.commit()
        
    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM stoklar WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults
        
    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM stoklar WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def Display(self):
        self.dbCursor.execute("SELECT * FROM stoklar")
        records = self.dbCursor.fetchall()
        return records

class Values:
    def Validate(self, id):
        if not (id.isdigit() ):
            return "id"
        else:
            return "SUCCESS"
        
class InsertWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.iconbitmap('icon.ico')
        self.window.wm_title("Stok Ekle")

        #Değişkenler
        self.id = tkinter.StringVar()
        self.s_ad = tkinter.StringVar()
        self.s_grup = tkinter.StringVar()
        self.s_birim = tkinter.StringVar()
        self.a_tarih = tkinter.StringVar()
        self.a_fiyat = tkinter.StringVar()
        self.s_fiyat = tkinter.StringVar()
        self.sg_miktar = tkinter.StringVar()
        self.m_miktar = tkinter.StringVar()
        self.t_ad = tkinter.StringVar()
        self.t_iletisim = tkinter.StringVar()


        # Label
        tkinter.Label(self.window, text = "Stok ID (*)",  width = 25).grid(pady = 5, column = 1, row = 1)
        tkinter.Label(self.window, text = "Stok Adı (*)",  width = 25).grid(pady = 5, column = 1, row = 2)
        tkinter.Label(self.window, text = "Stok Grubu",  width = 25).grid(pady = 5, column = 1, row = 3)
        tkinter.Label(self.window, text = "Stok Birimi",  width = 25).grid(pady = 5, column = 1, row = 4)
        tkinter.Label(self.window, text = "Alış Tarihi ",  width = 25).grid(pady = 5, column = 1, row = 5)
        tkinter.Label(self.window, text = "Alış Fiyatı",  width = 25).grid(pady = 5, column = 1, row = 6)
        tkinter.Label(self.window, text = "Satış Fiyatı",  width = 25).grid(pady = 5, column = 1, row = 7)
        tkinter.Label(self.window, text = "Stok Giriş Miktarı ",  width = 25).grid(pady = 5, column = 1, row = 8)
        tkinter.Label(self.window, text = "Mevcut Miktar",  width = 25).grid(pady = 5, column = 1, row = 9)
        tkinter.Label(self.window, text = "Tedarikçi Adı",  width = 25).grid(pady = 5, column = 1, row = 10)
        tkinter.Label(self.window, text = "Tedarikçi İletişim",  width = 25).grid(pady = 5, column = 1, row = 11)

        # Alanlar
        # Entry 
        self.idEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.id)
        self.s_adEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.s_ad)
        self.s_grupEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.s_grup)
        self.s_birimEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.s_birim)
        self.a_tarihEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.a_tarih)
        self.a_fiyatEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.a_fiyat)
        self.s_fiyatEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.s_fiyat)
        self.sg_miktarEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.sg_miktar)
        self.m_miktarEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.m_miktar)
        self.t_adEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.t_ad)
        self.t_iletisimEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.t_iletisim)
       


        self.idEntry.grid(pady = 5, column = 3, row = 1)
        self.s_adEntry.grid(pady = 5, column = 3, row = 2)
        self.s_grupEntry.grid(pady = 5, column = 3, row = 3)
        self.s_birimEntry.grid(pady = 5, column = 3, row = 4)
        self.a_tarihEntry.grid(pady = 5, column = 3, row = 5)
        self.a_fiyatEntry.grid(pady = 5, column = 3, row = 6)
        self.s_fiyatEntry.grid(pady = 5, column = 3, row = 7)
        self.sg_miktarEntry.grid(pady = 5, column = 3, row = 8)
        self.m_miktarEntry.grid(pady = 5, column = 3, row = 9)
        self.t_adEntry.grid(pady = 5, column = 3, row = 10)
        self.t_iletisimEntry.grid(pady = 5, column = 3, row = 11)
     


        # Buton
        tkinter.Button(self.window, width = 20, text = "Ekle", command = self.Insert).grid(pady = 15, padx = 5, column = 1, row = 14)
        tkinter.Button(self.window, width = 20, text = "Temizle", command = self.Reset).grid(pady = 15, padx = 5, column = 2, row = 14)
        tkinter.Button(self.window, width = 20, text = "Kapat", command = self.window.destroy).grid(pady = 15, padx = 5, column = 3, row = 14)

        self.window.mainloop()

    def Insert(self):
        self.values = Values()
        self.database = Database()
        self.test = self.values.Validate(self.idEntry.get())
        if (self.test == "SUCCESS"):
            self.database.Insert(self.idEntry.get(), self.s_adEntry.get(), self.s_grupEntry.get(), self.s_birimEntry.get(), self.a_tarihEntry.get(), self.a_fiyatEntry.get(), self.s_fiyatEntry.get(), self.sg_miktarEntry.get(), self.m_miktarEntry.get(), self.t_adEntry.get(),self.t_iletisimEntry.get())
            tkinter.messagebox.showinfo("Veri Eklendi", "Veriler başarıyla eklendi.")
        else:
            self.valueErrorMessage = self.test + "Alanında geçersiz değer girdiniz."
            tkinter.messagebox.showerror("Değer Hatası", self.valueErrorMessage)

    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.s_adEntry.delete(0, tkinter.END)
        self.s_grupEntry.delete(0, tkinter.END)
        self.s_birimEntry.delete(0, tkinter.END)
        self.a_tarihEntry.delete(0, tkinter.END)
        self.a_fiyatEntry.delete(0, tkinter.END)
        self.s_fiyatEntry.delete(0, tkinter.END)
        self.sg_miktarEntry.delete(0, tkinter.END)
        self.m_miktarEntry.delete(0, tkinter.END)
        self.t_adEntry.delete(0, tkinter.END)
        self.t_iletisimEntry.delete(0, tkinter.END)
     
    
class UpdateWindow:
    def __init__(self, id):
        self.window = tkinter.Tk()
        self.window.iconbitmap('icon.ico')
        self.window.wm_title("Veri Güncelle")

        # Initializing all the variables
        self.id = id

        self.s_ad = tkinter.StringVar()
        self.s_grup = tkinter.StringVar()
        self.s_birim = tkinter.StringVar()
        self.a_tarih = tkinter.StringVar()
        self.a_fiyat = tkinter.StringVar()
        self.s_fiyat = tkinter.StringVar()
        self.sg_miktar = tkinter.StringVar()
        self.m_miktar = tkinter.StringVar()
        self.t_ad = tkinter.StringVar()
        self.t_iletisim = tkinter.StringVar()
        

        # Labels
        tkinter.Label(self.window, text = "Stok ID (*)",  width = 25).grid(pady = 5, column = 1, row = 1)
        tkinter.Label(self.window, text = id,  width = 25).grid(pady = 5, column = 3, row = 1)
        tkinter.Label(self.window, text = "Stok Adı (*)",  width = 25).grid(pady = 5, column = 1, row = 2)
        tkinter.Label(self.window, text = "Stok Grubu",  width = 25).grid(pady = 5, column = 1, row = 3)
        tkinter.Label(self.window, text = "Stok Birimi",  width = 25).grid(pady = 5, column = 1, row = 4)
        tkinter.Label(self.window, text = "Alış Tarihi ",  width = 25).grid(pady = 5, column = 1, row = 5)
        tkinter.Label(self.window, text = "Alış Fiyatı",  width = 25).grid(pady = 5, column = 1, row = 6)
        tkinter.Label(self.window, text = "Satış Fiyatı",  width = 25).grid(pady = 5, column = 1, row = 7)
        tkinter.Label(self.window, text = "Stok Giriş Miktarı ",  width = 25).grid(pady = 5, column = 1, row = 8)
        tkinter.Label(self.window, text = "Mevcut Miktar",  width = 25).grid(pady = 5, column = 1, row = 9)
        tkinter.Label(self.window, text = "Tedarikçi Adı",  width = 25).grid(pady = 5, column = 1, row = 10)
        tkinter.Label(self.window, text = "Tedarikçi İletişim",  width = 25).grid(pady = 5, column = 1, row = 11)

        # Set previous values
        self.database = Database()
        self.searchResults = self.database.Search(id)
        
        tkinter.Label(self.window, text = self.searchResults[0][1],  width = 25).grid(pady = 5, column = 2, row = 2)
        tkinter.Label(self.window, text = self.searchResults[0][2],  width = 25).grid(pady = 5, column = 2, row = 3)
        tkinter.Label(self.window, text = self.searchResults[0][3],  width = 25).grid(pady = 5, column = 2, row = 4)
        tkinter.Label(self.window, text = self.searchResults[0][4],  width = 25).grid(pady = 5, column = 2, row = 5)
        tkinter.Label(self.window, text = self.searchResults[0][5],  width = 25).grid(pady = 5, column = 2, row = 6)
        tkinter.Label(self.window, text = self.searchResults[0][6],  width = 25).grid(pady = 5, column = 2, row = 7)
        tkinter.Label(self.window, text = self.searchResults[0][7],  width = 25).grid(pady = 5, column = 2, row = 8)
        tkinter.Label(self.window, text = self.searchResults[0][8],  width = 25).grid(pady = 5, column = 2, row = 9)
        tkinter.Label(self.window, text = self.searchResults[0][9],  width = 25).grid(pady = 5, column = 2, row = 10)
        tkinter.Label(self.window, text = self.searchResults[0][10],  width = 25).grid(pady = 5, column = 2, row = 11)
        
        

        # Alanlar
        # Entry 
        self.idEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.id)
        self.s_adEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.s_ad)
        self.s_grupEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.s_grup)
        self.s_birimEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.s_birim)
        self.a_tarihEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.a_tarih)
        self.a_fiyatEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.a_fiyat)
        self.s_fiyatEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.s_fiyat)
        self.sg_miktarEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.sg_miktar)
        self.m_miktarEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.m_miktar)
        self.t_adEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.t_ad)
        self.t_iletisimEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.t_iletisim)
        

        self.idEntry.grid(pady = 5, column = 3, row = 1)
        self.s_adEntry.grid(pady = 5, column = 3, row = 2)
        self.s_grupEntry.grid(pady = 5, column = 3, row = 3)
        self.s_birimEntry.grid(pady = 5, column = 3, row = 4)
        self.a_tarihEntry.grid(pady = 5, column = 3, row = 5)
        self.a_fiyatEntry.grid(pady = 5, column = 3, row = 6)
        self.s_fiyatEntry.grid(pady = 5, column = 3, row = 7)
        self.sg_miktarEntry.grid(pady = 5, column = 3, row = 8)
        self.m_miktarEntry.grid(pady = 5, column = 3, row = 9)
        self.t_adEntry.grid(pady = 5, column = 3, row = 10)
        self.t_iletisimEntry.grid(pady = 5, column = 3, row = 11)
    
        # Buton
        tkinter.Button(self.window, width = 20, text = "Güncelle", command = self.Update).grid(pady = 15, padx = 5, column = 1, row = 14)
        tkinter.Button(self.window, width = 20, text = "Temizle", command = self.Reset).grid(pady = 15, padx = 5, column = 2, row = 14)
        tkinter.Button(self.window, width = 20, text = "Kapat", command = self.window.destroy).grid(pady = 15, padx = 5, column = 3, row = 14)

        self.window.mainloop()

    def Update(self):
        self.database = Database()
        self.database.Update(self.s_adEntry.get(), self.s_grupEntry.get(), self.s_birimEntry.get(), self.a_tarihEntry.get(), self.a_fiyatEntry.get(), self.s_fiyatEntry.get(), self.sg_miktarEntry.get(), self.m_miktarEntry.get(), self.t_adEntry.get(), self.t_iletisimEntry.get(), self.id)
        tkinter.messagebox.showinfo("Veri Güncelleme", "Veriler başarıyla güncellendi")

    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.s_adEntry.delete(0, tkinter.END)
        self.s_grupEntry.delete(0, tkinter.END)
        self.s_birimEntry.delete(0, tkinter.END)
        self.a_tarihEntry.delete(0, tkinter.END)
        self.a_fiyatEntry.delete(0, tkinter.END)
        self.s_fiyatEntry.delete(0, tkinter.END)
        self.sg_miktarEntry.delete(0, tkinter.END)
        self.m_miktarEntry.delete(0, tkinter.END)
        self.t_adEntry.delete(0, tkinter.END)
        self.t_iletisimEntry.delete(0, tkinter.END)



class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.iconbitmap('icon.ico')
        self.databaseViewWindow.wm_title("Kayıtlar")

        # Label
        tkinter.Label(self.databaseViewWindow, text = "Kayıtlı Veriler",  width = 125, bg="#9FA8DA",font='Arial 10 bold').grid(pady = 1, column = 1, row = 1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady = 5, column = 1, row = 2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ("id", "s_ad", "s_grup", "s_birim", "a_tarih", "a_fiyat", "s_fiyat", "sg_miktar", "m_miktar", "t_ad", "t_iletisim")

        # Sütun Başlıkları
        self.databaseView.heading("id", text = "Stok ID")
        self.databaseView.heading("s_ad", text = "Stok Adı")
        self.databaseView.heading("s_grup", text = "Stok Grubu")
        self.databaseView.heading("s_birim", text = "Stok Birimi")
        self.databaseView.heading("a_tarih", text = "Alış Tarihi")
        self.databaseView.heading("a_fiyat", text = "Alış Fiyatı")
        self.databaseView.heading("s_fiyat", text = "Satış Fiyatı")
        self.databaseView.heading("sg_miktar", text = "Stok Giriş Miktarı")
        self.databaseView.heading("m_miktar", text = "Mevcut Miktar")
        self.databaseView.heading("t_ad", text = "Tedarikçi Adı")
        self.databaseView.heading("t_iletisim", text = "Tedarikçi İletişim")



        # Sütunlar
        self.databaseView.column("id", width = 100)
        self.databaseView.column("s_ad", width = 100)
        self.databaseView.column("s_grup", width = 100)
        self.databaseView.column("s_birim", width = 100)
        self.databaseView.column("a_tarih", width = 80)
        self.databaseView.column("a_fiyat", width = 60)
        self.databaseView.column("s_fiyat", width = 60)
        self.databaseView.column("sg_miktar", width = 100)
        self.databaseView.column("m_miktar", width = 100)
        self.databaseView.column("t_ad", width = 100)
        self.databaseView.column("t_iletisim", width = 100)
        

        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()

class SearchDeleteWindow:
    def __init__(self, task):
        window = tkinter.Tk()
        window.iconbitmap('icon.ico')
        window.wm_title("Stok " + task)
        window.geometry("450x100");

        self.id = tkinter.StringVar()
        self.s_ad = tkinter.StringVar()
        self.s_grup = tkinter.StringVar()
        
        # Label    
        tkinter.Label(window, text = "Stok Kodunu [Stok ID] Giriniz:", width = 30).grid(pady = 10, row = 1)
       
        # Entry
        self.idEntry = tkinter.Entry(window, width = 15, textvariable = self.id)

        self.idEntry.grid(pady = 35, column=1,row = 1)

        # Buton
    

        if (task == "Ara"):
            tkinter.Button(window, width = 10, text = task, command = self.Search).grid( padx = 15, column = 2, row = 1)
        elif (task == "Sil"):
            tkinter.Button(window, width = 10, text = task, command = self.Delete).grid( padx = 15, column = 2, row = 1)
        
           


    def Search(self):
        self.database = Database()
        self.data = self.database.Search(self.idEntry.get())
        self.databaseView = DatabaseView(self.data)
    
    def Delete(self):
        self.database = Database()
        self.database.Delete(self.idEntry.get())


#Anasayfa

class HomePage:
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("Stok Yönetim Sistemi")
        self.homePageWindow.iconbitmap('icon.ico')
        self.homePageWindow.configure(bg='#9FA8DA')
        self.homePageWindow.resizable(width=False, height=False)

        tkinter.Label(self.homePageWindow, text = "Stok Yönetim Sistemine Hoşgeldiniz.",font='Arial 10 bold',  width = 100, height=4, bg="#7986CB").grid(column = 0, row = 0)
       

        tkinter.Button(self.homePageWindow, width=30, height=2,bg="#C5CAE9",activebackground='#4CAF50', activeforeground='white', text = "Stok Ekle", command = self.Insert).grid(pady=10,padx=1 ,column = 0, row = 1)
        tkinter.Button(self.homePageWindow, width=30, height=2,bg="#C5CAE9",activebackground='#4CAF50', activeforeground='white', text = "Stok Güncelle", command = self.Update).grid(pady = 5,padx=1, column = 0, row = 2)
        tkinter.Button(self.homePageWindow, width=30, height=2,bg="#C5CAE9",activebackground='#4CAF50', activeforeground='white', text = "Stok Ara", command = self.Search).grid(pady = 5,padx=30, column = 0, row = 3)
        tkinter.Button(self.homePageWindow, width=30, height=2,bg="#C5CAE9",activebackground='#4CAF50', activeforeground='white', text = "Stok Sil", command = self.Delete).grid(pady = 5,padx=30,column = 0, row = 4)
        tkinter.Button(self.homePageWindow, width=50, height=2,bg="#C5CAE9",activebackground='#4CAF50', activeforeground='white', text = "Tüm Stokları Göster", command = self.Display).grid(pady = 5,padx=30 ,column = 0, row = 5)
        tkinter.Button(self.homePageWindow, width=50, height=2,bg="#C5CAE9",activebackground='#F44336', activeforeground='white', text = "Çıkış", command = self.homePageWindow.destroy).grid(pady = 5,padx=30 ,column = 0, row = 6)

        self.homePageWindow.mainloop()

    def Insert(self):
        self.insertWindow = InsertWindow()
    
    def Update(self):
        self.updateIDWindow = tkinter.Tk()
        self.updateIDWindow.wm_title("Stok Güncelle")
        self.updateIDWindow.iconbitmap('icon.ico')
        self.updateIDWindow.geometry("500x100");

        # Initializing all the variables
        self.id = tkinter.StringVar()

        # Label
        tkinter.Label(self.updateIDWindow, text = "Güncellenecek stoğun [Stok ID] bilgisini girin.", width = 40).grid(pady = 35, column = 0, row = 1)

        # Entry widgets
        self.idEntry = tkinter.Entry(self.updateIDWindow, width = 15, textvariable = self.id)  
        self.idEntry.grid(pady = 35, column=1 , row = 1)
        
        # Button widgets
        tkinter.Button(self.updateIDWindow, width = 10, text = "Getir", command = self.updateID).grid(padx =20, column= 3, row = 1)

        self.updateIDWindow.mainloop()

    def updateID(self):
        self.updateWindow = UpdateWindow(self.idEntry.get())
        self.updateIDWindow.destroy()

    def Search(self):
        self.searchWindow = SearchDeleteWindow("Ara")

    def Delete(self):
        self.deleteWindow = SearchDeleteWindow("Sil")

    def Display(self):
        self.database = Database()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)

homePage = HomePage()
