function getCurrentDateTime() {
    const now = new Date();
    
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    
    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}
// function VBDiShare(){
   
// }

function VBDenShare(){
    // Thu thập dữ liệu từ các thẻ input
    var idvanbanden = document.querySelector('.modal').getAttribute('id-vanban');
    var idnguoichuyen = document.querySelector('.id-canbo').textContent;
    var idnguoinhan= document.querySelector('.id-nguoinhan').selectedOptions[0].getAttribute('id-nguoinhan');
    // var thoigianchuyen = document.getElementById('current-datetime').textContent;
    var thoigianchuyen = getCurrentDateTime();
    var ykienchuyen = document.querySelector('.ip-note').value;
    
    // Tạo đối tượng FormData để gửi file đính kèm
    var butphe = new FormData();
    butphe.append('idVanBanDen', idvanbanden);
    butphe.append('idNguoiChuyen', idnguoichuyen);
    butphe.append('idNguoiNhan', idnguoinhan);
    butphe.append('ThoiGianChuyen', thoigianchuyen);
    butphe.append('YKienChuyen', ykienchuyen);
    

  console.log('YKienChuyen', ykienchuyen);
    // Gửi yêu cầu POST tới API /insert
    fetch('/hethong/vanbanden/chuyenpheduyet', {
        method: 'POST',
        body: butphe
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Chuyển phê duyệt thành công');
            // Reset form sau khi lưu thành công
            window.location.href = `/hethong/vanbanden/chitiet/${idnguoichuyen}/vb${idvanbanden}`;
        } else {
            alert('Chuyển phê duyệt thất bại: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Lỗi:', error);
        alert('Có lỗi xảy ra khi xử lý dữ liệu.');
    });
};