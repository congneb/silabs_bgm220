- Mặc định arduino-cli sẽ tạo folder .arduino15 ở /root folder
Nếu không dùng folder .arduino15 mặc định ở folder /root

- B0. Để xem folder .arduino15 mặc định nằm ở đâu
arduino-cli.exe config dump

- B1. Dùng lệnh sau để lấy file init
arduino-cli.exe config init --dest-dir E:\Soft\arduino-1.8.9-windows\arduino_cli<br>

1 file arduino-cli.yml sẽ được generate ra.<br>
Bạn cần sửa lại file này để dùng

- B2. Tạo folder chứa arduino lib
Ví dụ: Tôi muốn để nó ở folder này: E:\Soft\arduino-1.8.9-windows\arduino_cli

B2.1 Tạo folder PATH như sau<br>
E:\Soft\arduino-1.8.9-windows\arduino_cli\Arduino15\packages\SiliconLabs\hardware\siliconlabs\1.0.0

B2.2 clone arduino_staging repo về folder */*/1.0.0 ở trên

B2.3 Oke, done. Test thôi.<br>
arduino-cli.exe core list --config-file E:\Soft\arduino-1.8.9-windows\arduino_cli\arduino-cli.yaml

Nếu nó hiện kết quả như sau thì oke:<br>
ID                      Installed Latest Name<br>
SiliconLabs:siliconlabs 1.0.0     1.0.0  Silicon Labs

Or
arduino-cli.exe board listall bgm220 --config-file E:\Soft\arduino-1.8.9-windows\arduino_cli\arduino-cli.yaml
Board Name                          FQBN<br>
BGM220 Explorer Kit (BLE)           SiliconLabs:siliconlabs:bgm220explorerkit<br>
BGM220 Explorer Kit (BLE) (precomp) SiliconLabs:siliconlabs:bgm220explorerkit_precomp


- B3. Dowloads gcc12.2
B3.1 Tự tạo folder PATH như sau: E:\Soft\arduino-1.8.9-windows\arduino_cli\Arduino15\packages\SiliconLabs\tools\gcc-arm-none-eabi\12.2.rel1

Download về và giải nén vào đó.


- B4. Conpile example
set EXAMPLE_PATH=E:\Soft\arduino-1.8.9-windows\arduino_cli\Arduino15\packages\SiliconLabs\hardware\siliconlabs\1.0.0\libraries\ezBLE\examples\ezBLE_callbacks\ezBLE_callbacks.INO<br>
set CONFIG_PATH=E:\Soft\arduino-1.8.9-windows\arduino_cli\arduino-cli.yaml<br>
set ARD_LIB_DIR=E:\Soft\arduino-1.8.9-windows\arduino_cli\Arduino15\packages\SiliconLabs\hardware\siliconlabs\1.0.0<br>

arduino-cli.exe compile --config-file %CONFIG_PATH% -b SiliconLabs:siliconlabs:bgm220explorerkit_precomp %EXAMPLE_PATH% --output-dir E:\Soft\arduino-1.8.9-windows\arduino_cli\out --libraries %ARD_LIB_DIR%