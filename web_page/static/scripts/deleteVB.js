// Lấy danh sách các nút delete
const deleteButtons = document.querySelectorAll('.ti-btn-delete');

// Lặp qua từng nút delete và thêm sự kiện click
deleteButtons.forEach(button => {
    button.addEventListener('click', async () => {
        // Lấy idVanBanDi từ thuộc tính data-id của nút delete
        const idVanBanDi = button.getAttribute('deleteVanBanDi');

        // Gửi yêu cầu DELETE đến API endpoint
        try {
            const response = await fetch(`/hethong/vanbandi/delete?vb=${idVanBanDi}`, {
                method: 'DELETE',
            });

            // Xử lý phản hồi từ server
            if (response.ok) {
                const result = await response.json();
                console.log(result); // In ra kết quả từ server (thông báo và danh sách văn bản mới)

                // Cập nhật lại giao diện sau khi xóa thành công
                location.reload(); // Reload trang để cập nhật lại danh sách
            } else {
                console.error('Không thể xóa văn bản');
            }
        } catch (error) {
            console.error('Lỗi khi gửi yêu cầu DELETE:', error);
        }
    });
});




const deleteVBDen_Buttons = document.querySelectorAll('.ti-btn-delete-VBDen');

deleteVBDen_Buttons.forEach(button => {
    button.addEventListener('click', async () => {
        // Lấy idVanBanDen từ thuộc tính data-id-vanbanden của thẻ <i>
        const idVanBanDen = button.getAttribute('data-id-vanbanden');
        console.log(idVanBanDen);
        // Gửi yêu cầu DELETE đến API endpoint
        try {
            const response = await fetch(`/hethong/vanbanden/delete/id=${idVanBanDen}`, {
                method: 'DELETE',
            });

            // Xử lý phản hồi từ server
            if (response.ok) {
                const result = await response.json();
                console.log(result); // In ra kết quả từ server (thông báo và danh sách văn bản mới)

                // Cập nhật lại giao diện sau khi xóa thành công
                location.reload(); // Reload trang để cập nhật lại danh sách
            } else {
                console.error('Không thể xóa văn bản');
            }
        } catch (error) {
            console.error('Lỗi khi gửi yêu cầu DELETE:', error);
        }
    });
});

