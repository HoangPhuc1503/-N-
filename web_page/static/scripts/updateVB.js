


function updateVBDi(){

    document.addEventListener("DOMContentLoaded", function() {
        
        var updateButton = document.getElementById('btn-updatevb');
    
        updateButton.addEventListener('click', function() {
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
            var LinkFileVanBan = document.querySelector('.vb-file-name').textContent;
            var TrangThaiXuLy = document.querySelector('.ip-trangthai').selectedOptions[0].getAttribute('id-trangthaixuly');
            var idVanBanDi = parseInt(document.querySelector('.right-content-form').getAttribute('id-vanbandi'));
            
            
            var formData = {};
            formData["idNguoiPheDuyet"] = parseInt(idNguoiPheDuyet);
            formData["idHinhThuc"] = parseInt(idHinhThuc);
            formData["idLinhVuc"] = parseInt(idLinhVuc);
            formData["idDoKhanCap"] = parseInt(idDoKhanCap);
            formData["idLoaiVanBan"] = parseInt(idLoaiVanBan);
            formData["idCanBo"] = parseInt(idCanBo);
            formData["HanXuLy"] = HanXuLy;
            formData["TrichYeu"] = TrichYeu;
            formData["SoDen"] = parseInt(SoDen);
            formData["NgayPhatHanh"] = NgayPhatHanh;
            formData["SoKyHieu"] = SoKyHieu;
            formData["LinkFileVanBan"] = LinkFileVanBan;
            formData["TrangThaiXuLy"] = parseInt(TrangThaiXuLy);
            formData["idVanBanDi"] = idVanBanDi;
    
            console.log(formData);
            // Gửi yêu cầu POST tới API /capnhatvanban
            fetch(`/hethong/vanbandi/update/${idCanBo}/vb${idVanBanDi}`, {
                method: 'PUT',
                body: JSON.stringify(formData)
            })
            .then(response =>{
                if (response.status === 200) {
                    alert('Chỉnh sửa thông tin văn bản thành công!');
                    // Reset form sau khi lưu thành công
                    document.querySelector('.right-content-form').reset();
                } else {
                    throw new Error('Chỉnh sửa thông tin văn bản không thành công!');
                }
            })
            .catch(error => {
                console.error('Lỗi:', error);
                alert('Có lỗi xảy ra khi chỉnh sửa dữ liệu.');
            });
        });
    });
    
};


function updateVBDen(){

    document.addEventListener("DOMContentLoaded", function() {


        var savevbDen_Button = document.getElementById('btn-vbden');
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

            var idCanBo = document.querySelector('.id-canbo').textContent;
            var idVanBanDen = document.getElementById('right-main-content_1').getAttribute('id-VanBanDen');
    
            var FileVanBan = document.querySelector('.vbDen-file-name').textContent;
            var LinkFileVanBan = document.getElementById('filevb').files[0];
            // var LinkFileVanBan = document.querySelector('#filevb').files[0];
            // // Kiểm tra nếu file chưa được chọn
            

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
            formDatakvbd.append('idVanBanDenn', idVanBanDen);
            formDatakvbd.append('fileVanBan', FileVanBan);
            // formDatakvbd.append('linkFileVanBan', LinkFileVanBan);
            if (LinkFileVanBan !== undefined) {
                formDatakvbd.append('linkFileVanBan', LinkFileVanBan);
            }
            // } else {
            //     formData.append('linkFileVanBan', "None");
            // }
            

            var formDataEntries = formDatakvbd.entries();

            // Duyệt qua từng cặp giá trị và hiển thị chúng
            for (const pair of formDataEntries) {
                console.log(pair[0] + ', ' + pair[1]);
            }

            // Gửi yêu cầu PUT tới API /capnhatvanban
            fetch(`/hethong/vanbanden/update/${idCanBo}/vb${idVanBanDen}`, {
                method: 'PUT',
                body: formDatakvbd
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Cập nhật văn bản thành công!');
                    // Reset form sau khi lưu thành công
                    // document.querySelector('.right-content-form').reset();
                    // window.location.href = `/hethong/vanbanden?id=${idCanBo}`;
                } else {
                    alert('Cập nhât văn bản không thành công: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Lỗi:', error);
                alert('Có lỗi xảy ra khi lưu dữ liệu.');
            });
        });
    });
};

// Cập nhật văn bản


updateVBDi();
updateVBDen();
