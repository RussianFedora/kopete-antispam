Name:           kopete-antispam
Version:        0.5
Release:        2%{?dist}
Summary:        Antispam plugin for Kopete
Summary(ru):    Антиспам плагин для Kopete

License:        GPLv2+
URL:            http://kopeteantispam.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/kopeteantispam/kopeteantispam/0.5/%{name}-kde4-%{version}.tar.gz

BuildRequires:  kdenetwork-kopete-devel
BuildRequires:  qt-devel
BuildRequires:  openssl-devel
BuildRequires:  libX11-devel

%description
Kopete plugin, which allows to ignore spam messages by using simple
by using simple answer/question scheme:
Potential spammers receive a simple question, and they are ignored until
they answers question. After they answers correctly, they receive
notification, and your chat window opens. Also, you can skip test for
some contacts, matched by wildcards, specified by configuration dialog.

%description -l ru
Плагин для Kopete, который позволяет игнорировать спам-сообщения, используя
простую схему вопрос/ответ:
потенциальные спамеры получают простой вопрос, и игнорируются, пока не дадут
на него ответ. После того как правильный ответ дан, они получают уведомление,
и окно чата откроется.

%prep
%setup -q -n %{name}-kde4-%{version}


%build
%{cmake_kde4}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%{_libdir}/kde4/*kopete_antispam*
%{_datadir}/config.kcfg/kopeteantispamconfig.kcfg
%{_datadir}/kde4/services/kconfiguredialog/kopete_antispam_config.desktop
%{_datadir}/kde4/services/kopete_antispam.desktop


%changelog
* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5-2.R
- Added description in russian language

* Wed Nov 02 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.5-1.R
- initla build
