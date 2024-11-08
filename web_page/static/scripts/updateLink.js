// Lấy danh sách các nút update
const updateButtons = document.querySelectorAll('.ti-btn-update');

// Lặp qua từng nút delete và thêm sự kiện click
updateButtons.forEach(button => {
    button.addEventListener('click', async () => {
        // Lấy idVanBanDi từ thuộc tính data-id của nút delete
        const idCanBo = document.querySelector('.id-canbo').textContent;
        const idVanBanDi = button.getAttribute('updateVanBanDi');

        window.location.href = `/hethong/vanbandi/update/${idCanBo}/vb${idVanBanDi}`;
    });
});



// Lấy danh sách các nút update văn bản đến
const updateButtonsVBD = document.querySelectorAll('.ti-btn-update-VBD');

// Lặp qua từng nút delete và thêm sự kiện click
updateButtonsVBD.forEach(button => {
    button.addEventListener('click', async () => {
        // Lấy idVanBanDi từ thuộc tính data-id của nút delete
        const idCanBo = document.querySelector('.id-canbo').textContent;
        const idVanBanDen = button.getAttribute('idVanBanden');

        window.location.href = `/hethong/vanbanden/update/${idCanBo}/vb${idVanBanDen}`;
    });
});
