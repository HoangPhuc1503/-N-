function themvanbandi(){
    document.addEventListener("DOMContentLoaded", function() {
        var saveButton = document.getElementById('btn-themmoivb');
    
        saveButton.addEventListener('click', function(event) {
            event.preventDefault();
            // Thu thập dữ liệu từ các thẻ input
            var idNguoiPheDuyet = document.querySelector('.ip-nguoipheduyet').selectedOptions[0].getAttribute('id-nguoipheduyet');
            var idHinhThuc = document.querySelector('.ip-hinhthuc').selectedOptions[0].getAttribute('id-hinhthucvb');
            var idLinhVuc = document.querySelector('.ip-linhvuc').selectedOptions[0].getAttribute('id-linhvucvb');
            var idDoKhanCap = document.querySelector('.ip-dokhan').selectedOptions[0].getAttribute('id-dokhanvb');
            var idLoaiVanBan = document.querySelector('.ip-loaivanban').selectedOptions[0].getAttribute('id-loaivb');
            var idCanBo = document.querySelector('.id-canbo').textContent;
            var HanXuLy = document.querySelector('.ip-hanxuly').value;
            var TrichYeu = document.querySelector('.ip-trichyeu').value;
            var SoDen = document.querySelector('.ip-soden').value;
            var NgayPhatHanh = document.querySelector('.ip-ngayphathanh').value;
            var SoKyHieu = document.querySelector('.ip-sokyhieu').value;
            var LinkFileVanBan = document.querySelector('#filevb').files[0];
            var TrangThaiXuLy = document.querySelector('.ip-trangthai').selectedOptions[0].getAttribute('id-trangthaixuly');
            // Lấy nội dung của thẻ span có class="user-name"
            
    
            // Tạo đối tượng FormData để gửi file đính kèm
            var formData = new FormData();
            formData.append('idNguoiPheDuyet', idNguoiPheDuyet);
            formData.append('idHinhThuc', idHinhThuc);
            formData.append('idLinhVuc', idLinhVuc);
            formData.append('idDoKhanCap', idDoKhanCap);
            formData.append('idLoaiVanBan', idLoaiVanBan);
            formData.append('idCanBo', idCanBo);
            formData.append('HanXuLy', HanXuLy);
            formData.append('TrichYeu', TrichYeu);
            formData.append('SoDen', SoDen);
            formData.append('NgayPhatHanh', NgayPhatHanh);
            formData.append('SoKyHieu', SoKyHieu);
            formData.append('fileVanBan', LinkFileVanBan);
            formData.append('TrangThaiXuLy', TrangThaiXuLy);
            // formData.append('vanBanCanXuLy', vanBanCanXuLy);
                
            // Gửi yêu cầu POST tới API /insert
            fetch('/hethong/vanbandi/insert', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Thêm mới văn bản thành công!');
                    // Reset form sau khi lưu thành công
                    document.querySelector('.right-content-form').reset();
                    window.location.href = `/hethong/vanbandi?id=${idCanBo}`;
                } else {
                    alert('Thêm mới văn bản không thành công: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Lỗi:', error);
                alert('Có lỗi xảy ra khi lưu dữ liệu.');
            });
        });
    });
    
};


function themvanbanden(){
    document.addEventListener("DOMContentLoaded", function() {
        var savevbDen_Button = document.getElementById('btn-themmoivbden');
        savevbDen_Button.addEventListener('click', function() {
            // Lấy các giá trị từ các trường form
            var TrichYeu = document.querySelector(".abstract_input").value;
            var idHinhThuc = document.querySelector('#form_cb').selectedOptions[0].getAttribute('id-hinhthucvb');
            var DonViBanHanh = document.querySelector(".issuing_unit_input").value;
            var SoDen = document.querySelector(".incoming_number_input").value;
            var idLinhVuc = document.querySelector('#field_cb').selectedOptions[0].getAttribute('id-linhvucvb');
            var idTinhChatVanBan = document.querySelector('#textual_properties_cb').selectedOptions[0].getAttribute('id-tinhchatvanban');
            var idKhoa = document.querySelector('#Department_cb').selectedOptions[0].getAttribute('id-Khoa');
            var NgayDen = document.querySelector(".ip-ngayden").value;
            var NgayBanHanh = document.querySelector(".ip-ngaybanhanh").value;
            var SoKyHieu = document.querySelector(".symbol_number_input").value;
            var idCanBoDuyet = document.querySelector('#position_cb').selectedOptions[0].getAttribute('id-nguoipheduyet');
            var idDoKhanCap = document.querySelector('#Urgency_cb').selectedOptions[0].getAttribute('id-dokhanvb');
            var idLoaiVanBan = document.querySelector('#Document_Type_cb').selectedOptions[0].getAttribute('id-loaiVB');
            var idNguoiNhap = document.querySelector(".id-canbo").textContent.trim();
            var needAnswer = document.querySelector('input[name="need_answer"]:checked').value;
            var needHandle = document.querySelector('input[name="need_handle"]:checked').value;
            var HanTraLoi = document.querySelector(".ip-ngaytraloi").value;
            var SoNgay = document.querySelector(".number_days_input").value;
            var idTrangThaiVanBan = document.querySelector('#reply_status_cb').selectedOptions[0].getAttribute('id-trangthaixuly');
            var LinkFileVanBan = document.querySelector('#filevb').files[0];
    
            // Kiểm tra nếu file chưa được chọn
            if (!LinkFileVanBan) {
                alert('Vui lòng chọn file đính kèm.');
                return;
            }
    
            // Tạo đối tượng FormData và thêm các trường
            var formDatakvbd = new FormData();
            formDatakvbd.append('TrichYeu', TrichYeu);
            formDatakvbd.append('idHinhThuc', idHinhThuc);
            formDatakvbd.append('DonViBanHanh', DonViBanHanh);
            formDatakvbd.append('SoDen', SoDen);
            formDatakvbd.append('idLinhVuc', idLinhVuc);
            formDatakvbd.append('idTinhChatVanBan', idTinhChatVanBan);
            formDatakvbd.append('idKhoa', idKhoa);
            formDatakvbd.append('NgayDen', NgayDen);
            formDatakvbd.append('NgayBanHanh', NgayBanHanh);
            formDatakvbd.append('SoKyHieu', SoKyHieu);
            formDatakvbd.append('idCanBoDuyet', idCanBoDuyet);
            formDatakvbd.append('idDoKhanCap', idDoKhanCap);
            formDatakvbd.append('idLoaiVanBan', idLoaiVanBan);
            formDatakvbd.append('idNguoiNhap', idNguoiNhap);
            formDatakvbd.append('needAnswer', needAnswer);
            formDatakvbd.append('needHandle', needHandle);
            formDatakvbd.append('HanTraLoi', HanTraLoi);
            formDatakvbd.append('SoNgay', SoNgay);
            formDatakvbd.append('idTrangThaiVanBan', idTrangThaiVanBan);
            formDatakvbd.append('fileVanBan', LinkFileVanBan);
    
            // Gửi dữ liệu form bằng fetch API
            fetch('/hethong/vanbanden/insert', {
                method: 'POST',
                body: formDatakvbd
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Thêm mới văn bản thành công!');
                    // Reset form sau khi lưu thành công
                    // document.querySelector('.right-content-form').reset();
                    window.location.href = `/hethong/vanbanden?id=${idNguoiNhap}`;
                } else {
                    alert('Thêm mới văn bản không thành công: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Lỗi:', error);
                alert('Có lỗi xảy ra khi lưu dữ liệu.');
            });
        });
    });
};

//Thêm văn bản 

themvanbandi();
themvanbanden();
