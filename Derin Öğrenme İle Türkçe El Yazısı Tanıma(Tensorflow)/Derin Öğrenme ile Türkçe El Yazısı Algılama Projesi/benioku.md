-----------------------------------------------------------ALİ SAİD GÜNEŞ--------------------------------------------------

-----------------------------------------------------------FATİH HAKAN MEHMET ÇAYLIDEMİRCİ-------------------------------------------------

-----------------------------------------------------------FURKAN DURSUN-------------------------------------------------


AŞAMALAR

1- Daha önce yapılmış örnekler var mı varsa nasıl yapıldığını anlamak için araştırdık
2- Araştırmalarımız sonucunda Deep Learning ve Machine Learning mantığını anlamaya karar verdik ve bu sebeple bir kurs belirledik ve kursun üzerinden ilerledik
3- Kurstan sonra herbirimiz daha önce yapılmış farklı projeleri denedik
4- NIST datasetini inceledik ve eğitmeye çalıştık
5- Başarısız olunca IAM datasetinde karar kıldık ve https://github.com/githubharald/SimpleHTR adresindeki projeyi temel aldık
6- Bu projeyi çalıştırdığımızda IAM datasetinin sadece İngilizce karakterler içerdiğini gördük ve Türkçe karakterleri nasıl ekleyeceğimizi araştırdık
7- Bunun için bu adresteki https://towardsdatascience.com/faq-build-a-handwritten-text-recognition-system-using-tensorflow-27648fb18519? adımları uygulamaya karar verdik
8- İlk olarak bilgisayar fontu ile 80.000 civarı Türkçe kelime içereren dataset oluşturduk ve  etiketledik bunun sonucunda Türkçe karakterleri tanımlayabildik
9- Ancak kelimeler bilgisayar fontu ile yazıldığı için modelimiz el yazısını tahmin edemedi
10- Buyüzden kendi datasetimizi oluşturmaya karar verdik, çevremizden ve bir okuldan el yazısı kelimeler ve harfler topladık ve bunları resimleyip etiketledik
11- Dataseti hallettikten sonra modelimizi GPU (NVIDIA 1650) ile en iyi sonuca ulaşıncaya kadar eğittik

KARŞILAŞTIĞIMIZ SORUNLAR VE ÇÖZÜMLERİ

1- Projeyi test ederken assertion ve  epochs ile ilgili hatalar aldık
2- Türkçe Dataset oluştururken ingilizcede olmayan harflerin sembollerle ifade edildiğini gördük ve projedeki uygun yerlere "encoding utf-8" değerini atadık
3- Modelimizi eğitirken err"mismatch...." hatası aldık bunun için modelin daha önceki eğitiminden kalan dosyaları silip tekrar eğitince hatayı çözdük
4- Dataseti oluştururken opencv ingilizce dışındaki Türkçe karakterleri tanımadığı için pillow kütüphanesini kullandık
5- Dataset için veri topladığımızda resimler IAM datasetindeki formatta değildi bunun için resimleri opncv ile bazı işlemlerden geçirdik



PROJEYİ ÇALIŞTIRMA

1- Proje klasöründeki Kelime Tespiti ve OpenCV İşlemleri adlı klasörleri masaüstüne atın
2- Test etmek istediğiniz resmi OpenCV işlemleri klasörüne atın ve hepsi.py'nin içine ilgili kısma resim adını ve uzantısını girin
3- Resmi işledikten sonra yine aynı klasörde bulunan segmentation içerisinden işlenmiş resimlerden test etmek istediğinizi seçin ve Kelime Tespiti klasöründeki data klasörü içine resmi atın
4- Kelime Tespiti klasöründeki src klasöründen main.py'yi açın ve 18. satırdaki fnInfer'e resmin adını örnekteki gibi yazın  daha sonra  editörden veya cmd'den python main.py diyerek çalıştırın (spyder editöründe tekrar çalışıtırırsanız restart kernel yapmanız gerekir)


Not: Proje/Kelime Tespiti/Test klasöründeki resimleri test edebilrsiniz



GEREKLİ SÜRÜMLER

---- OpenCv = 3.31
---- Tensorflow = 1.14
---- Python 3.6.9
