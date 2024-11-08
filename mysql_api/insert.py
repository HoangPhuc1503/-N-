from conn import connection

#văn bản đi
def themmoivanban(vanban):
    connect = connection()
    if connect.is_connected():
        cursor = connect.cursor()
        try:
            # Lưu trữ dữ liệu vào bảng 'vanbandi'
            for item in vanban:
                query = "INSERT INTO VanBanDi (idNguoiPheDuyet, idHinhThuc, idLinhVuc, idDoKhanCap, idLoaiVanBan, idCanBo, HanXuLy, TrichYeu, SoDen, NgayPhatHanh, SoKyHieu, LinkFileVanBan, TrangThaiXuLy) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (item['idNguoiPheDuyet'], item['idHinhThuc'], item['idLinhVuc'], item['idDoKhanCap'], item['idLoaiVanBan'], item['idCanBo'], item['HanXuLy'], item['TrichYeu'], item['SoDen'], item['NgayPhatHanh'], item['SoKyHieu'], item['LinkFileVanBan'], item['TrangThaiXuLy']))
                


            # Commit thay đổi vào cơ sở dữ liệu
            connect.commit()
            print("Dữ liệu đã được lưu vào cơ sở dữ liệu thành công!")
        except Exception as e:
            print("Lỗi khi lưu trữ dữ liệu:", e)
            # Rollback nếu có lỗi xảy ra
            connect.rollback()
        finally:
            # Đóng cursor và kết nối
            cursor.close()
            connect.close()
            print("Kết nối đến cơ sở dữ liệu đã được đóng.")


def butphelanhdao(butphe):
    connect = connection()
    if connect.is_connected():
        cursor = connect.cursor()
        try:

            for item in butphe:
                    query = """
                        INSERT INTO ButPheLanhDao (idVanBanDi, idNguoiChuyen, idNguoiNhan, ThoiGianChuyen, YKienChuyen)
                        VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (
                        item['idVanBanDi'], item['idNguoiChuyen'], item['idNguoiNhan'], 
                        item['ThoiGianChuyen'], item['YKienChuyen']
                    ))
            
            # Commit thay đổi vào cơ sở dữ liệu
            connect.commit()
            print("Dữ liệu đã được lưu vào cơ sở dữ liệu thành công!")
        except Exception as e:
            print("Lỗi khi lưu trữ dữ liệu:", e)
            # Rollback nếu có lỗi xảy ra
            connect.rollback()
        finally:
            # Đóng cursor và kết nối
            cursor.close()
            connect.close()
            print("Kết nối đến cơ sở dữ liệu đã được đóng.")



#văn bản đi
def updateTrangThai(vanban):
    connect = connection()
    if connect.is_connected():
        cursor = connect.cursor()
        try:
            # Lưu trữ dữ liệu vào bảng 'vanbandi'
            for item in vanban:
                query2 = "UPDATE VanBanDi SET TrangThaiXuLy = %s WHERE LinkFileVanBan = %s"
                cursor.execute(query2, (item['TrangThaiXuLy'], item['LinkFileVanBan']))


            # Commit thay đổi vào cơ sở dữ liệu
            connect.commit()
            print("Dữ liệu đã được lưu vào cơ sở dữ liệu thành công!")
        except Exception as e:
            print("Lỗi khi lưu trữ dữ liệu:", e)
            # Rollback nếu có lỗi xảy ra
            connect.rollback()
        finally:
            # Đóng cursor và kết nối
            cursor.close()
            connect.close()
            print("Kết nối đến cơ sở dữ liệu đã được đóng.")





# văn bản đến
def themmoivanbanden(vanbanden):
    connect = connection()
    if connect.is_connected():
        cursor = connect.cursor()
        try:
            # Lưu trữ dữ liệu vào bảng 'VanBanDen'
            for item in vanbanden:
                query = """
                INSERT INTO VanBanDen (
                    idHinhThuc, DonViBanHanh, SoDen, idLinhVuc, TinhChatVB, idDoKhanCap, 
                    LoaiVanBan, NgayDen, NgayPhatHanh, SoKyHieu, idCanBo, idNguoiPheDuyet, 
                    idKhoa, CanTraLoiVB, CanXuLyVB, HanTraLoi, SoNgay, LinkFileVanBan, 
                    TrichYeu, TrangThaiXuLy
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
                    item['idTrangThaiVanBan']
                ))
            # Commit thay đổi vào cơ sở dữ liệu
            connect.commit()
            print("Dữ liệu đã được lưu vào cơ sở dữ liệu thành công!")
            return True
        except Exception as e:
            print("Lỗi khi lưu trữ dữ liệu:", e)
            # Rollback nếu có lỗi xảy ra
            connect.rollback()
            return False
        finally:
            # Đóng cursor và kết nối
            cursor.close()
            connect.close()
            print("Kết nối đến cơ sở dữ liệu đã được đóng.")
    return False


def butphelanhdaoVbDen(vanbanden):
    connect = connection()
    if connect.is_connected():
        cursor = connect.cursor()
        try:
            # Lưu trữ dữ liệu vào bảng 'butphelanhdao'
            for item in vanbanden:
                query = "INSERT INTO ButPheLanhDao (idVanBanDen, idNguoiChuyen, idNguoiNhan, ThoiGianChuyen, YKienChuyen) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (item['idVanBanDen'], item['idNguoiChuyen'], item['idNguoiNhan'], item['ThoiGianChuyen'], item['YKienChuyen']))
            
                query2 = "UPDATE VanBanDen SET idNguoiPheDuyet = %s WHERE idVanBanDen = %s"
                cursor.execute(query2, (item['idNguoiNhan'], item['idVanBanDen']))
            # Commit thay đổi vào cơ sở dữ liệu
            connect.commit()
            print("Dữ liệu đã được lưu vào cơ sở dữ liệu thành công!")
        except Exception as e:
            print("Lỗi khi lưu trữ dữ liệu:", e)
            # Rollback nếu có lỗi xảy ra
            connect.rollback()
        finally:
            # Đóng cursor và kết nối
            cursor.close()
            connect.close()
            print("Kết nối đến cơ sở dữ liệu đã được đóng.")