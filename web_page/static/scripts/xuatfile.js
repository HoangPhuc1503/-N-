document.addEventListener("DOMContentLoaded", function() {
    var Btn_exportfile = document.getElementById("btn-export-filePDF");

    Btn_exportfile.addEventListener("click", function() {
        // Thu thập dữ liệu từ các phần tử `span`
        var trich_yeu = document.querySelector('.ip-trichyeu').innerText;
        var lanh_dao_phe_duyet = document.querySelector('.ip-nguoipheduyet').innerText;
        var so_ky_hieu = document.querySelector('.ip-sokyhieu').innerText;
        var so_den = document.querySelector('.ip-soden').innerText;
        var loai_van_ban = document.querySelector('.ip-loaivanban').innerText;
        var ngay_ban_hanh = document.querySelector('.ip-ngayphathanh').innerText;
        var han_xu_ly = document.querySelector('.ip-hanxuly').innerText;
        var linh_vuc = document.querySelector('.ip-linhvuc').innerText;
        var do_khan = document.querySelector('.ip-dokhan').innerText;

        var filename = document.querySelector('.ip-filename').innerText;
       
        // Tạo một đối tượng chứa dữ liệu
        var data = {
            trich_yeu: trich_yeu,
            lanh_dao_phe_duyet: lanh_dao_phe_duyet,
            so_ky_hieu: so_ky_hieu,
            so_den: so_den,
            loai_van_ban: loai_van_ban,
            ngay_ban_hanh: ngay_ban_hanh,
            han_xu_ly:han_xu_ly,
            linh_vuc: linh_vuc,
            do_khan: do_khan,
            filename: filename,
        };

        // Gửi yêu cầu POST đến API
        fetch(`/export_pdf`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                // Nếu kết quả trả về thành công, trả về file PDF từ phản hồi
                return response.blob();
            } else {
                // Nếu có lỗi xảy ra, xử lý lỗi
                throw new Error('Lỗi khi xuất PDF');
            }
        })
        .then(blob => {
            // Tạo một URL cho file PDF
            var url = URL.createObjectURL(blob);
            // Mở file PDF trong một tab mới
            window.open(url);
        })
        .catch(error => {
            // Xử lý lỗi
            console.error('Lỗi kết nối:', error);
        });
    });
});
