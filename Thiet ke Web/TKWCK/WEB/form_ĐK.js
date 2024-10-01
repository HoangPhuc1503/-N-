function kiemtra_ĐK() {
    var c = document.getElementById("email").value;
    var c1 = document.getElementById("username").value;
    var c2 = document.getElementById("password").value;
    if (c == "") {
        alert("Vui lòng nhập email của bạn !");
    } else if (c1 == "") {
        alert("Vui lòng nhập tên đăng nhập !");
    } else if (c2 == "") {
        alert("Vui lòng nhập mật khẩu !");
    } else {
        // alert("Xin hãy điền đúng thông tin !");
        return true;
    }
}