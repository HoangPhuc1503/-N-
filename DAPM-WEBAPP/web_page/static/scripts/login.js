
document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("form-login");
    
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Ngăn chặn việc gửi form đi
        
        const formData = new FormData(loginForm);
        const tenDN = formData.get("tenDN");
        const mK = formData.get("mK");
        
        if (tenDN.trim() !== "" && mK.trim() !== "") {
            // Đăng nhập thành công
            window.location.href = `/checklogin?tenDN=${tenDN}&mK=${mK}`;
            // Thực hiện các hành động khác ở đây, chẳng hạn chuyển hướng đến trang chính sau khi đăng nhập thành công
        } else {
            alert("Vui lòng nhập tên đăng nhập và mật khẩu.");
        }
    });
});
