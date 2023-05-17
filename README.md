# Danh sách thành viên
Họ Tên|Lớp|Email
-|-|-
Nguyễn Lê Quốc Bảo|11CA3|baobao150106@gmail.com

# Thông tin project
## Đề tài: 
Web app tăng cường việc học tiếng Anh
## Sơ lược về app
- Chức năng 1 - `Translator`: có thể định vị chữ tiếng Anh trong file pdf chứa hình ảnh (có thể file pdf sách, tài liệu) và dịch ra ngôn ngữ tiếng Việt cho người dùng
- Chức năng 2 - `Spelling`: Chức năng này như một trò chơi giúp người dùng phát huy vốn từ và cách đánh vần, viết đúng chính tả từ vựng đó. Khi chọn `random word now` thì sẽ xuất hiện một từ tiếng Anh ngẫu nhiên và cho biết độ dài từ (length) và một từ có ngữ nghĩa gần từ đó nhất. Nếu người chơi chưa đoán ngay được từ được random thì có thể chọn `more relevant word` để xuất hiện nhiều từ khác liên quan. Tuy nhiên sẽ bị trừ điểm, và nếu người chơi bỏ cuộc, chọn `reveal the word` và từ sẽ xuất hiện và tất nhiên điểm trả về 0. Khi đó người chơi phải viết tay từ đó để tăng cường việc ghi nhớ và kiểm tra két quả cũng như học nghĩa của từ mới.

## Các thư viện sử dụng: 
`Pillow, pytesseract, pdf2image, googletrans, streamlit-drawable-canvas, opencv-python, scikit-image, keras, wordhoard, nltk`

## Các chức năng chính & kế hoạch thực hiện

Chức năng|Người thực hiện|Ngày hoàn thành dự kiến
-|-|-
Convolutional Neural Network (CNN) for hand-written letters classification|Nguyễn Lê Quốc Bảo|9/05/2023
Build the Translator and web UI|Nguyễn Lê Quốc Bảo|9/05/2023
Build the UI for hand-writing canvas and CNN on Streamlit|Nguyễn Lê Quốc Bảo|10/05/2023
Dictionary function|Nguyễn Lê Quốc Bảo|10/05/2023
App deployment and Demo video|Nguyễn Lê Quốc Bảo|11/05/2023

## Code Structure

        final_project
        ├── CNN_model
        │   ├── app
        │   ├── CNN_model.h5
        │   ├── CNN_model.h5.png
        │   ├── CNN_model_for_hand_written_letters_classification.ipynb
        ├── Streamlit_app
        │   ├── app.py
        │   ├── sidebar.py
        │   ├── spelling_panel.py
        │   └── word_scrapping.py
        ├── README.md
        └── wordhoard_error.yaml

## Video Demo
https://www.youtube.com/watch?v=M0zUddo8rOU&t=4s
