from conn import connection

def capnhatthongtincb(thongtincanhan):
    connect = connection()
    if connect.is_connected():
        cursor = connect.cursor()
        try:
            # Lưu trữ dữ liệu vào bảng 'vanbandi'
            for item in thongtincanhan:
                query = "UPDATE CanBo SET HoTen = %s , SDT = %s, Email = %s, CCCD = %s , GioiTinh = %s, DiaChi = %s, GioiThieu = %s  WHERE idCanBo = %s "
                cursor.execute(query, (item['tencanbo'], item['sodienthoai'], item['email'], item['cccd'], item['gioitinh'], item['diachi'], item['gioithieu'], item['idCanBo']))
            # Commit thay đổi vào cơ sở dữ liệu
            connect.commit()
            print("Dữ liệu đã được cập nhật vào cơ sở dữ liệu thành công!")
        except Exception as e:
            print("Lỗi khi lưu trữ dữ liệu:", e)
            # Rollback nếu có lỗi xảy ra
            connect.rollback()
        finally:
            # Đóng cursor và kết nối
            cursor.close()
            connect.close()
            print("Kết nối đến cơ sở dữ liệu đã được đóng.")


def capnhatvanban(vanban):
    connect = connection()
    if connect.is_connected():
        cursor = connect.cursor()
        try:
            # Cập nhật dữ liệu vào bảng 'VanBanDi'
            for item in vanban:
                query = """
                UPDATE VanBanDi
                SET idNguoiPheDuyet = %s,
                    idHinhThuc = %s,
                    idLinhVuc = %s,
                    idDoKhanCap = %s,
                    idLoaiVanBan = %s,
                    idCanBo = %s,
                    HanXuLy = %s,
                    TrichYeu = %s,
                    SoDen = %s,
                    NgayPhatHanh = %s,
                    SoKyHieu = %s,
                    LinkFileVanBan = %s,
                    TrangThaiXuLy = %s
                WHERE idVanBanDi = %s
                """
                cursor.execute(query, (
                    item['idNguoiPheDuyet'], 
                    item['idHinhThuc'], 
                    item['idLinhVuc'], 
                    item['idDoKhanCap'], 
                    item['idLoaiVanBan'], 
                    item['idCanBo'], 
                    item['HanXuLy'], 
                    item['TrichYeu'], 
                    item['SoDen'], 
                    item['NgayPhatHanh'], 
                    item['SoKyHieu'], 
                    item['LinkFileVanBan'], 
                    item['TrangThaiXuLy'], 
                    item['idVanBanDi']
                ))
            # Commit thay đổi vào cơ sở dữ liệu
            connect.commit()
            print("Dữ liệu đã được cập nhật vào cơ sở dữ liệu thành công!")
        except Exception as e:
            print("Lỗi khi cập nhật dữ liệu:", e)
            # Rollback nếu có lỗi xảy ra
            connect.rollback()
        finally:
            # Đóng cursor và kết nối
            cursor.close()
            connect.close()
            print("Kết nối đến cơ sở dữ liệu đã được đóng.")




# Văn bản đến
def capnhatvanbanden(vanbanden):
    connect = connection()
    if connect.is_connected():
        cursor = connect.cursor()
        try:
            # Lưu trữ dữ liệu vào bảng 'VanBanDen'
            for item in vanbanden:
                query = """
                UPDATE VanBanDen
                SET
                    idHinhThuc= %s, DonViBanHanh= %s, SoDen= %s, idLinhVuc= %s, TinhChatVB= %s, idDoKhanCap= %s, 
                    LoaiVanBan= %s, NgayDen= %s, NgayPhatHanh= %s, SoKyHieu= %s, idCanBo= %s, idNguoiPheDuyet= %s, 
                    idKhoa= %s, CanTraLoiVB= %s, CanXuLyVB= %s, HanTraLoi= %s, SoNgay= %s, LinkFileVanBan= %s, 
                    TrichYeu= %s, TrangThaiXuLy= %s WHERE idVanBanDen = %s
                """
                cursor.execute(query, (
                    item['idHinhThuc'], 
                    item['DonViBanHanh'], 
                    item['SoDen'], 
                    item['idLinhVuc'], 
                    item['idTinhChatVanBan'], 
                    item['idDoKhanCap'], 
                    item['idLoaiVanBan'],                            
                    item['NgayDen'], 
                    item['NgayBanHanh'], 
                    item['SoKyHieu'], 
                    item['idNguoiNhap'], 
                    item['idCanBoDuyet'], 
                    item['idKhoa'],
                    item['needAnswer'], 
                    item['needHandle'], 
                    item['HanTraLoi'], 
                    item['SoNgay'], 
                    item['LinkFileVanBan'], 
                    item['TrichYeu'], 
                    item['idTrangThaiVanBan'],
                    item["idVanBanDenn"]
                ))
            # Commit thay đổi vào cơ sở dữ liệu
            connect.commit()
            print("Dữ liệu đã được cập nhật vào cơ sở dữ liệu thành công!")
            return True
        except Exception as e:
            print("Lỗi khi cập nhật dữ liệu:", e)
            # Rollback nếu có lỗi xảy ra
            connect.rollback()
            return False
        finally:
            # Đóng cursor và kết nối
            cursor.close()
            connect.close()
            print("Kết nối đến cơ sở dữ liệu đã được đóng.")
    return False




def update_ChucVu(idCanBo: int, idQuyenTruyCap: int):
    try:
        connect = connection()
        with connect.cursor() as cursor:
            cursor.execute("UPDATE CanBo SET idQuyenTruyCap = %s WHERE idCanBo = %s", (idQuyenTruyCap,idCanBo,))
            connect.commit()
            return {"message": f"Phan quyen thanh cong"}
    except Exception as e:
        print("Lỗi khi cập nhật dữ liệu:", e)
            # Rollback nếu có lỗi xảy ra
        connect.rollback()
        return False
    finally:
            # Đóng cursor và kết nối
        cursor.close()
        connect.close()
        print("Kết nối đến cơ sở dữ liệu đã được đóng.")