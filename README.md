# Image-based-breed-recognition-for-cattle-and-buffaloes-of-India





---

## 📌 Problem Description  
- Breed identification errors often occur due to **manual judgment** and **lack of breed-specific awareness** among FLWs.  
- India has a **large variety of indigenous and crossbred cattle and buffalo breeds**, making identification challenging.  
- Incorrect entries compromise:  
  - Genetic improvement programs  
  - Nutrition planning  
  - Disease control measures  
  - Overall program outcomes  

---

## 🎯 Proposed Solution  
An **AI-driven solution** that can identify cattle and buffalo breeds using images. This will:  

✅ Use **image recognition + machine learning** to standardize identification  
✅ Handle **diverse backgrounds, lighting, and animal poses**  
✅ Maintain a **breed database** (common Indian cattle & buffalo breeds and crosses)  
✅ Provide **real-time breed suggestions** during registration in BPA  
✅ Seamlessly **integrate with the BPA platform**  
✅ Offer a **user-friendly interface** requiring minimal training for FLWs  

---

## 🛠️ Tech Stack  
- **Python 3**  
- **Ultralytics YOLOv8 (Classification mode)**  
- **NumPy**  
- **Custom dataset of cattle and buffalo breeds**  

---

## 📂 Dataset Structure  
The dataset should follow the YOLO classification format:  

dataset/
│── train/
│    ├── Aryshire/
│    ├── Brown/
│    ├── Dane/
│    ├── Friesian/
│    ├── Jersey/
│── val/
│    ├── Aryshire/
│    ├── Brown/
│    ├── Dane/
│    ├── Friesian/
│    ├── Jersey/
│── test/
│    ├── Aryshire/
│    ├── Brown/
│    ├── Dane/
│    ├── Friesian/
│    ├── Jersey/



---



##1️⃣ Clone the Repository & Install Dependencies  
```bash
git clone https://github.com/sundram6452/Image-based-breed-recognition-for-cattle-and-buffaloes-of-India.git
cd Image-based-breed-recognition-for-cattle-and-buffaloes-of-India
pip install ultralytics numpy
python catt.py

```

##📊 Example Output
Top Predictions:
Friesian: 95.34%
Jersey: 3.12%
Brown: 1.02%
Aryshire: 0.32%
Dane: 0.20%
