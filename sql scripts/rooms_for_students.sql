create database rooms_for_students

go
create table Rooms(
Id_room int primary key not null,
name_room nvarchar(255) not null)

go
create table Students(
birthday_student datetime,
Id_student int primary key not null,
name_student nvarchar(255),
room_student int not null,
sex nvarchar(1))

go
alter table Students add constraint cfk foreign key(room_student) references Rooms(Id_room) on delete cascade

go
alter table Students add constraint csex check (sex in ('M', 'F'));

--indices
go
create index students_in_rooms_idx ON Students(room_student)

go
create index age_of_students_idx ON Students(room_student, birthday_student)

go
create index students_sex_idx ON Students(room_student, sex)
