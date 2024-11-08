function convertDateFormat(datestr) {
    try {
        // Kiểm tra xem ngày có định dạng DD/MM/YYYY không
        const datePattern1 = /^\d{2}\/\d{2}\/\d{4}$/;
        if (datePattern1.test(datestr)) {
            // Nếu không có lỗi, trả về ngày gốc
            return datestr;
        }
        // Nếu có lỗi, có nghĩa là ngày không đúng định dạng DD/MM/YYYY
        const datePattern2 = /^\d{4}-\d{2}-\d{2}$/;
        if (datePattern2.test(datestr)) {
            // Chuyển đổi chuỗi ngày sang đối tượng Date theo định dạng YYYY-MM-DD
            const [year, month, day] = datestr.split('-');
            // Chuyển đổi đối tượng Date sang chuỗi ngày định dạng DD/MM/YYYY
            return `${day}/${month}/${year}`;
        } else {
            throw new Error('Invalid date format');
        }
    } catch (e) {
        // Xử lý lỗi nếu ngày không đúng định dạng
        console.error(`Error converting date: ${e.message}`);
        return null;
    }
}

const ngayPhatHanhElement = document.querySelector(".ip-ngayphathanh");
const ngayPhatHanh = ngayPhatHanhElement.textContent.trim();
ngayPhatHanhElement.textContent = convertDateFormat(ngayPhatHanh);

const hanxulyElement = document.querySelector(".ip-hanxuly");
const hanxuly = hanxulyElement.textContent.trim();
hanxulyElement.textContent = convertDateFormat(hanxuly);