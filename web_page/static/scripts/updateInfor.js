document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".custom_button").addEventListener("click", function() {
        var idcanbo = parseInt(document.querySelector(".id-canbo").textContent);
        
        var tencanbo = document.querySelector(".name_input").value;
        var gioitinh = document.querySelector("input[name='gender']:checked").value;
        var cccd = document.querySelector(".CCCD_input").value;
        var sdt = document.querySelector(".Phonenumber_input").value;
        var email = document.querySelector(".Email_input").value;
        var diachi = document.querySelector(".Address_input").value;
        var gioithieu = document.querySelector(".Introduce_input").value;
        
        var formData = {};
        formData["idCanBo"] = idcanbo;
        formData["tencanbo"] = tencanbo;
        formData["gioitinh"] = gioitinh;
        formData["cccd"] = cccd;
        formData["sodienthoai"] = sdt;
        formData["email"] = email;
        formData["diachi"] = diachi;
        formData["gioithieu"] = gioithieu;
        
        fetch(`/hethong/thongtincanhan/update/${idcanbo}`, {
            method: 'PUT',
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (response.status === 200) {
                alert("cập nhật thông tin cá nhân thành công");
                window.location.href = `/hethong/thongtincanhan?id=${idcanbo}`;
            } else {
                throw new Error('Có lỗi xảy ra khi cập nhật thông tin!');
            }
        })
        .catch(error => {
            console.error('Lỗi:', error);
            // Hiển thị thông báo lỗi hoặc thực hiện các hành động cần thiết khác để thông báo cho người dùng về lỗi
        });
    });
});
