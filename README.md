# Education Prediction

## NASIL ÇALIŞTIRILIR?
### Repo'yu klonlayın ve çalıştırmak için uygulama klasörünü açın.

# PROJE İNCELEMESİ

Bu proje, eğitim verileri kullanılarak yetişkin okuryazarlık oranını tahmin etmeyi amaçlayan bir uygulama barındırır. KNeighborsRegressor modelini kullanarak, kullanıcıdan alınan eğitim harcamaları ve okuryazarlık oranına etki eden diğer eğitim göstergeleriyle yetişkin okuryazarlık oranını tahmin etmektedir.

Projenin geliştirilmesine Kaggle'dan alınan "world-education-data.csv" verisiyle başlanıldı. Bu veri seti, birçok eğitim göstergesini içermektedir.

### Veri İşleme ve Model Kurma
* Veri Temizliği: Eksik değerler, sütunların ortalamaları ile dolduruldu.
* Öznitelik Seçimi: "ülke", "ülke_kodu" ve "yıl" gibi gereksiz sütunlar çıkarıldı. Modelde yalnızca eğitimle ilgili gösterge değişkenleri kullanıldı.
* Özellik Ölçekleme: Verinin daha doğru işlenmesi için eğitim verisi standartlaştırıldı.
* Model Seçimi: Bir çok model denendikten sonra, en doğru skoru veren ve en hızlı çalışan model olarak KNeighborsRegressor tercih edildi. Ardından GridSearchCV ile en iyi parametreler belirlendi ve model son haline getirildi.
## Kullanıcı Arayüzü
Uygulama, kullanıcıdan eğitim harcamaları, ilköğretim tamamlanma oranı, öğretmen-öğrenci oranları gibi  eğitim göstergelerini alarak yetişkin okuryazarlık oranı tahmini yapmaktadır. Uygulama, Tkinter kütüphanesi kullanılarak geliştirilip, görselleştirme için de Matplotlib ile tahmin sonuçlarını kullanıcıya gösteren bir grafik sunar.

## Kullanıcı Arayüzü Özellikleri:

* Kullanıcı, her bir eğitim göstergesi için varsayılan değerler veya kendi değerlerini girer.
* Kullanıcı "Tahmin Et" butonuna tıklayarak tahmin sonucu alır.
* Sistem, tahmin edilen değeri ekranda gösterir ve tahmin geçmişini günceller.
* Uygulama, her yeni tahminin ardından sonuçları görsel olarak sunar.
## Kullanıcı Girişi
Uygulama, kullanıcıdan aşağıdaki göstergeler için giriş alır:

* Eğitim Harcamaları (GSYİH)
* İlköğretim Tamamlama Oranı
* İlköğretim Öğrenci-Öğretmen Oranı
* Ortaöğretim Öğrenci-Öğretmen Oranı
* İlköğretim Kayıt Oranı
* Ortaöğretim Kayıt Oranı
* Yükseköğretim Kayıt Oranı
* Model Parametreleri
* Model: KNeighborsRegressor
* Parametre Optimizasyonu: GridSearchCV kullanılarak en iyi parametreler belirlendi.


---
# Education Prediction

## HOW TO RUN THE APPLICATION?
Clone the repository and open the project folder to run it.

### PROJECT REVIEW

This project hosts an application aimed at predicting adult literacy rates using education data. The application uses KNeighborsRegressor to predict the adult literacy rate based on educational expenditures and other educational indicators provided by the user.

The development of the project started with the dataset "world-education-data.csv" sourced from Kaggle. This dataset contains numerous educational indicators.

### Data Processing and Model Building
* **Data Cleaning:** Missing values were filled with the mean values of the columns.
* **Feature Selection:** Unnecessary columns like "country", "country_code", and "year" were removed. Only education-related indicator variables were included in the model.
* **Feature Scaling:** The training data was standardized for more accurate model performance.
* **Model Selection:** After testing several models, KNeighborsRegressor was chosen as the model that provided the most accurate score and provided the best performance. The optimal results were determined using GridSearchCV, and the model was finalized.

### User Interface
The application estimates the adult literacy rate by accepting educational indicators such as educational expenditures, primary school completion rates, teacher-student ratios, etc., from the user. The application provides a graph showing the user's predictions using Matplotlib with Tkinter support for visualization and development.

### User Interface Features:

* The user enters either default values or their own values for each educational indicator.
* The user clicks the "Predict" button to get the prediction result.
* The system displays the predicted value on the screen and updates the prediction log.
* The application presents the results visually after each new prediction.

### User Input
The application takes input from the user for the following indicators:

* Educational Expenditure (GDP)
* Primary School Completion Rate
* Primary School Student-Teacher Ratio
* Secondary School Student-Teacher Ratio
* Primary School Enrollment Rate
* Secondary School Enrollment Rate
* Higher Education Enrollment Rate
* Model Parameters
* Model: KNeighborsRegressor
* Parameter Optimization: The optimal parameters were determined using the GridSearchCV method.
