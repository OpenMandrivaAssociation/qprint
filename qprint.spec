Summary:	Encode and decode quoted printable data
Name:           qprint
Version:        1.0
Release:        %mkrel 6
License:        Public Domain
Group:		Networking/Mail
URL:		http://www.fourmilab.ch/webtools/qprint/
Source:         %{name}-%{version}.tar.bz2

%description
qprint is a command line utility which encodes and decodes
files in this format. It can be used within a pipeline as
an encoding or decoding filter, and is most commonly used
in this manner as part of an automated mail processing
system. With appropriate options, qprint can encode pure
binary files, but it's a poor choice since it may inflate
the size of the file by as much as a factor of three. The
base64 MIME encoding is a better choice for such data. 

%prep

%setup -q

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m755 qprint %{buildroot}%{_bindir}/
install -m755 qprint.1 %{buildroot}%{_mandir}/man1/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README index.html logo.gif qprint.pdf rfc1521.*
%{_bindir}/qprint
%{_mandir}/man1/qprint.1*
