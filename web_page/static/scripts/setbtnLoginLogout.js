document.addEventListener("DOMContentLoaded", function() {
    // Lấy HoTen từ localStorage
    // const hoTen = localStorage.getItem('HoTen');
    const hoTen = document.getElementById("user-name");
    
    if (hoTen) {

        const authLink = document.getElementById("auth-link");
        authLink.href = "/logout"

        const authName = document.getElementById("auth-name");
        authName.textContent = "Đăng xuất"
    } else {
        // Trường hợp không có HoTen trong localStorage
        console.error('Không tìm thấy thông tin người dùng.');
    }
});
