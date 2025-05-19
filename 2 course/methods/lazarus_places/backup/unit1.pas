unit Unit1;

{$mode objfpc}{$H+}
{$codepage UTF8}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls,
  Menus, sqlite3conn, sqldb, DB, LCLType, FPImage, FPReadPNG, FPReadJPEG, IniFiles, Unit2;

type
  { TForm1 }
  TForm1 = class(TForm)
    ListBox1: TListBox;
    LabelName: TLabel;
    ImageDirector: TImage;
    MemoDesc: TMemo;
    MainMenu1: TMainMenu;
    MenuItemHelp: TMenuItem;
    MenuItemContent: TMenuItem;
    MenuItemSeparator: TMenuItem;
    MenuItemAbout: TMenuItem;
    SQLite3Connection1: TSQLite3Connection;
    SQLTransaction1: TSQLTransaction;
    SQLQuery1: TSQLQuery;
    procedure FormCreate(Sender: TObject);
    procedure FormClose(Sender: TObject; var CloseAction: TCloseAction);
    procedure ListBox1SelectionChange(Sender: TObject);
    procedure MenuItemContentClick(Sender: TObject);
    procedure MenuItemAboutClick(Sender: TObject);
  private
    procedure LoadSettings;
    procedure SaveSettings;
    procedure LoadExplorers;
    procedure ShowExplorerInfo(ExplorerID: Integer);
    function CheckDatabaseStructure: Boolean;
    procedure CreateDatabase(const DBPath: string);
    procedure LoadImageToTImage(const FileName: string; DestImage: TImage);
    procedure FormKeyDown(Sender: TObject; var Key: Word; Shift: TShiftState);
  public
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.LoadSettings;
var
  Ini: TIniFile;
begin
  Ini := TIniFile.Create(ExtractFilePath(Application.ExeName) + 'AmDBMSF.INI');
  try
    Top := Ini.ReadInteger('main', 'top', 100);
    Left := Ini.ReadInteger('main', 'left', 100);
    Width := 800;
    Height := 500;

    if Ini.ReadBool('main', 'screencenter', True) then
      Position := poScreenCenter
    else
      Position := poDesigned;
  finally
    Ini.Free;
  end;
end;

procedure TForm1.SaveSettings;
var
  Ini: TIniFile;
begin
  Ini := TIniFile.Create(ExtractFilePath(Application.ExeName) + 'AmDBMSF.INI');
  try
    Ini.WriteInteger('main', 'top', Top);
    Ini.WriteInteger('main', 'left', Left);
    Ini.WriteInteger('main', 'width', Width);
    Ini.WriteInteger('main', 'height', Height);
    Ini.WriteBool('main', 'screencenter', Position = poScreenCenter);
    Ini.WriteString('main', 'datapath', 'Москва златоглавая');
    Ini.WriteString('main', 'about', '(c) Историко-географическое сообщество');
  finally
    Ini.Free;
  end;
end;

procedure TForm1.LoadImageToTImage(const FileName: string; DestImage: TImage);
var
  Picture: TPicture;
begin
  if not FileExists(FileName) then
    raise Exception.Create('Файл не найден: ' + FileName);

  Picture := TPicture.Create;
  try
    try
      Picture.LoadFromFile(FileName);
      DestImage.Picture.Assign(Picture);
    except
      on E: Exception do
        raise Exception.Create('Ошибка загрузки изображения: ' + E.Message);
    end;
  finally
    Picture.Free;
  end;
end;

function TForm1.CheckDatabaseStructure: Boolean;
var
  TableExists: Boolean;
begin
  Result := False;
  try
    SQLQuery1.Close;
    SQLQuery1.SQL.Text := 'SELECT name FROM sqlite_master WHERE type=''table'' AND name=''places''';
    SQLQuery1.Open;
    TableExists := not SQLQuery1.EOF;
    SQLQuery1.Close;

    if not TableExists then
    begin
      ShowMessage('Таблица places не найдена в базе данных!');
      Exit;
    end;

    SQLQuery1.SQL.Text := 'PRAGMA table_info(places)';
    SQLQuery1.Open;

    while not SQLQuery1.EOF do
      SQLQuery1.Next;

    SQLQuery1.Close;
    Result := True;
  except
    on E: Exception do
    begin
      ShowMessage('Ошибка при проверке структуры БД: ' + E.Message);
      Result := False;
    end;
  end;
end;

procedure TForm1.CreateDatabase(const DBPath: string);
var
  PhotosDir: string;
begin
  try
    // Создаем папку для фотографий
    PhotosDir := ExtractFilePath(Application.ExeName) + 'images';
    if not DirectoryExists(PhotosDir) then
      CreateDir(PhotosDir);

    SQLite3Connection1.DatabaseName := DBPath;
    SQLite3Connection1.Connected := True;
    SQLTransaction1.Active := True;

    SQLQuery1.SQL.Text :=
      'CREATE TABLE places (' +
      'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
      'name TEXT NOT NULL, ' +
      'description TEXT NOT NULL, ' +
      'image_path TEXT NOT NULL);';
    SQLQuery1.ExecSQL;

    SQLQuery1.SQL.Text :=
      'INSERT INTO places (name, description, image_path) VALUES ' +
      '("Красная площадь","Красная площадь в Москве — сердце российской столицы, исторический и культурный центр города.", "red_square.jpg"), ' +
      '("Петергоф", "Петергоф — знаменитый дворцово-парковый ансамбль в пригороде Санкт-Петербурга.", "peterhof.jpg"), ' +
      '("Казанский Кремль", "Казанский Кремль — древний памятник архитектуры и истории Татарстана.", "kazan_kremlin.jpg"), ' +
      '("Эрмитаж", "Один из крупнейших и старейших музеев искусства в мире. Эрмитаж включает коллекции произведений искусства, археологических находок и культурных артефактов. Этот музей является не только историческим, но и культурным центром России.", "hermitage.jpg"), ' +
      '("Кремль", "Один из самых известных исторических объектов в России, символ власти. Кремль в Москве — это комплекс зданий, который был резиденцией русских царей, а затем и советских руководителей. Внутри Кремля находятся несколько соборов, знаменитые башни, а также Троицкий собор и Царь-пушка.", "kremlin.jpeg"), ' +
      '("Соловецкие острова", "Соловецкий монастырь был важным религиозным центром в России, а в советский период стал известен как место для ГУЛАГа. Соловецкие острова сегодня привлекают туристов своими историческими монастырями, природными красотами и памятниками.", "images/solovki.jpg"), ' +
      '("Валаамский монастырь", "Валаамский архипелаг в северной части России — это один из самых древних монастырей, основанный в XVI веке. Монастырь на Валааме является важным духовным и культурным центром.", "images/valaam.jpg"), ' +
      '("Новгородский кремль", "Великий Новгород — колыбель русской государственности. Новгородский Кремль, с его древними стенами и башнями, а также Софийским собором, является свидетельством вековой истории Руси и важнейшим памятником средневековой архитектуры.", "images/novgorod_kremlin.jpg"), ' +
      '("Суздаль", "Суздаль — это часть Золотого кольца России, знаменитый своими древними монастырями, храмами и архитектурными памятниками. Суздаль был важным центром в истории средневековой Руси, и его архитектура сохранилась в первозданном виде.", "images/suzdal.jpeg"), ' +
      '("Троице-Сергиева лавра (Сергиев Посад)", "Один из самых известных монастырей России и важный духовный центр. Лавра была основана в XIV веке святого Сергия Радонежского и долгое время была местом, куда приходили верующие за духовной помощью и обучением.", "images/sergiev_posad.jpg")';

    SQLQuery1.ExecSQL;

    SQLTransaction1.Commit;
  except
    on E: Exception do
    begin
      ShowMessage('Ошибка при создании базы данных: ' + E.Message);
      SQLTransaction1.Rollback;
    end;
  end;
end;

procedure TForm1.ShowExplorerInfo(ExplorerID: Integer);
var
  PhotoPath: string;
begin
  try
    SQLQuery1.Close;
    SQLQuery1.SQL.Text := 'SELECT * FROM places WHERE id = :id';
    SQLQuery1.ParamByName('id').AsInteger := ExplorerID;
    SQLQuery1.Open;

    if not SQLQuery1.EOF then
    begin
      LabelName.Caption := SQLQuery1.FieldByName('name').AsString;
      MemoDesc.Text := SQLQuery1.FieldByName('description').AsString;

      PhotoPath := IncludeTrailingPathDelimiter(ExtractFilePath(Application.ExeName)) +
                  'images' + PathDelim +
                  SQLQuery1.FieldByName('image_path').AsString;

      try
        LoadImageToTImage(PhotoPath, ImageDirector);
      except
        on E: Exception do
        begin
          if FileExists('images/no_image.png') then
            LoadImageToTImage('images/no_image.png', ImageDirector)
          else
            ImageDirector.Picture.Clear;
        end;
      end;
    end;

    SQLQuery1.Close;
  except
    on E: Exception do
      ShowMessage('Ошибка: ' + E.Message);
  end;
end;

procedure TForm1.FormKeyDown(Sender: TObject; var Key: Word; Shift: TShiftState);
begin
  if Key = VK_F1 then
  begin
    ShowMessage('Известные исторические места России' + LineEnding +
             'Версия 1.0' + LineEnding +
             '©Ustyantsev, Moscow, 2025' + LineEnding + LineEnding + 'Большое спасибо моим родителям: Устьянцеву Дмитрию Аркадьевичу и Устьянцевой Маргарите Шамсумовной за их поддержку и любовь!');
    Key := 0;
  end;
end;

procedure TForm1.FormCreate(Sender: TObject);
var
  DBPath, PhotosDir: string;
begin
  Constraints.MinWidth := 550;
  Constraints.MinHeight := 550;

  KeyPreview := True;
  OnKeyDown := @FormKeyDown;


  LoadSettings;


  ImageDirector.Proportional := True;
  ImageDirector.Center := True;

  try

    PhotosDir := ExtractFilePath(Application.ExeName) + 'images';
    if not DirectoryExists(PhotosDir) then
      CreateDir(PhotosDir);


    DBPath := ExtractFilePath(Application.ExeName) + 'places.db';

    if not FileExists(DBPath) then
    begin
      CreateDatabase(DBPath);
      ShowMessage('База данных успешно создана!');
    end;

    SQLite3Connection1.DatabaseName := DBPath;
    SQLite3Connection1.Connected := True;
    SQLTransaction1.Active := True;

    if CheckDatabaseStructure then
      LoadExplorers;
  except
    on E: Exception do
      ShowMessage('Ошибка инициализации: ' + E.Message);
  end;
end;

procedure TForm1.FormClose(Sender: TObject; var CloseAction: TCloseAction);
begin
  SaveSettings;
end;


procedure TForm1.LoadExplorers;
begin
  try
    SQLQuery1.Close;
    SQLQuery1.SQL.Text := 'SELECT id, name FROM places ORDER BY name';
    SQLQuery1.Open;

    ListBox1.Items.Clear;
    while not SQLQuery1.EOF do
    begin
      ListBox1.Items.AddObject(SQLQuery1.FieldByName('name').AsString,
        TObject(PtrInt(SQLQuery1.FieldByName('id').AsInteger))
      );
      SQLQuery1.Next;
    end;
    SQLQuery1.Close;
  except
    on E: Exception do
      ShowMessage('Ошибка загрузки списка: ' + E.Message);
  end;
end;

procedure TForm1.ListBox1SelectionChange(Sender: TObject);
begin
  if ListBox1.ItemIndex >= 0 then
    ShowExplorerInfo(PtrInt(ListBox1.Items.Objects[ListBox1.ItemIndex]));
end;

procedure TForm1.MenuItemContentClick(Sender: TObject);
begin
  if not Assigned(Form2) then
    Form2 := TForm2.Create(Application);

  Form2.Show;
  Form2.BringToFront;
end;

procedure TForm1.MenuItemAboutClick(Sender: TObject);
begin
  ShowMessage('ИЗВЕСТНЫЕ ИСТОРИЧЕСКИЕ МЕСТА РОССИИ' + LineEnding +
             'Версия 1.0' + LineEnding +
             'Ustyantsev, Moscow, 2025');
end;

end.
