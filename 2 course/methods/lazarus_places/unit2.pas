unit Unit2;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TForm2 }

  TForm2 = class(TForm)
    Memo1: TMemo;
    procedure FormCreate(Sender: TObject);
  private

  public

  end;

var
  Form2: TForm2;

implementation

{$R *.lfm}

{ TForm2 }

procedure TForm2.FormCreate(Sender: TObject);
begin
   Memo1.Text := '10 ИЗВЕСТНЫХ ИСТОРИЧЕСКИХ МЕСТ РОССИИ...' + LineEnding + LineEnding +
             'Функции:' + LineEnding +
             '1. Просмотр списка известных исторических мест...' + LineEnding +
             '2. Информация о них...' + LineEnding +
             '3. Фотографии мест...';
  Memo1.ReadOnly := True;
  Caption := 'Содержание...';
  BorderStyle := bsSingle;
  BorderIcons := [biSystemMenu];
  Position := poScreenCenter;
  Constraints.MinWidth := Width;
  Constraints.MaxWidth := Width;
  Constraints.MinHeight := Height;
  Constraints.MaxHeight := Height;

end;



end.

