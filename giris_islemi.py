  
sys_kullanıcıadı="semih"  #kullanıcı adı ve şifteyi istediğiniz gibi değiştirebilirsiniz
sys_parola="12345"

giriş_hakkı=3

while True:
    kullanıcı_adı = input("Kullanıcı adınızı giriniz:")
    parola= input("Parolanızı giriniz:")
    if (kullanıcı_adı !=sys_kullanıcıadı and parola == sys_parola):
        print("Kullanıcı adı hatalı")
        giriş_hakkı -=1
    elif (kullanıcı_adı == sys_kullanıcıadı and parola != sys_parola):
        print("şifreyi yanlış girdiniz")
        giriş_hakkı -=1
    elif (kullanıcı_adı != sys_kullanıcıadı and parola != sys_parola):
        print("Kullanıcı adı ve parola hatalı")
        giriş_hakkı -=1
        
    else:
        print("Sisteme başarılı şekilde girildi")
        break
    if (giriş_hakkı == 0):
        print("Giriş hakkınız bitti.")
        break
