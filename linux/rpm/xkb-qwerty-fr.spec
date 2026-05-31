Name:           xkb-qwerty-fr
Version:        0.7.3
Release:        1%{?dist}
Summary:        Qwerty keyboard layout with French accents
Group:          System Environment/Base

License:        MIT
URL:            https://github.com/qwerty-fr/qwerty-fr
BuildArch:      noarch
Source0:        us_qwerty-fr
Source1:        keymap.txt
Source2:        LICENSE
Source3:        qwerty-fr.7
Source4:        evdev.xml
BuildRequires:  pkgconfig(xkbcommon) >= 1.13
Requires:       libxkbcommon >= 1.13
Requires:       xkeyboard-config >= 2.45

%global xkb_extensions_root %(pkg-config --variable=xkb_unversioned_extensions_path xkbcommon 2>/dev/null || printf '%s' %{_datadir}/xkeyboard-config.d)
%global xkb_package_dir %{xkb_extensions_root}/%{name}

%description
Keyboard layout based on the QWERTY layout with extra symbols and diacritics so
that typing both in French and English is easy and fast.
It is also easy to learn!

%prep

%build

%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{xkb_package_dir}/symbols/us
install -Dpm 0644 %{SOURCE4} %{buildroot}%{xkb_package_dir}/rules/evdev.xml
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/keymap.txt
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_licensedir}/%{name}/LICENSE

install -d %{buildroot}%{_mandir}/man7
gzip -c9 %{SOURCE3} > %{buildroot}%{_mandir}/man7/qwerty-fr.7.gz

%files
%license %{_licensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/keymap.txt
%{_mandir}/man7/qwerty-fr.7.gz
%{xkb_package_dir}/symbols/us
%{xkb_package_dir}/rules/evdev.xml

%changelog
* Sun Dec 10 2023 Paul <devnoname120@gmail.com> - 0.7.3-1
- xkb-qwerty-fr (0.7.3) unstable; urgency=low

    * Layout: Replaced 〉 with ⟩ in the math mode. i.e. “Right Angle
      Bracket” was replaced with “Mathematical Right Angle Bracket”.
      〉 is the “Right Angle Bracket” but we actually want ⟩ which is the
      “Mathematical Right Angle Bracket”.
    * Linux: Removed parasitic .DS_Store/__MACOSX/DEBIAN files from the Linux
      package.
    * Linux: Changed the separator characters used in keymap.txt to improve
      readability. Credits go to https://github.com/eclipseo

* Tue Sep 06 2022 Paul <devnoname120@gmail.com> - 0.7.2-1
- xkb-qwerty-fr (0.7.2) unstable; urgency=low

    * Linux: Fixed syntax error that broke the layout. Credits go to
      https://github.com/SimonGaufreteau.

* Sat Jul 23 2022 Paul <devnoname120@gmail.com> - 0.7.1-1
- xkb-qwerty-fr (0.7.1) unstable; urgency=low

    * Layout: Swapped the position of dead currency (¤) and euro sign (€) to
      make the latter more accessible as it's very frequently used in European
      countries.
    * MacOS: Fixed many issues.
    * Windows: Fixed many issues.

* Wed Jun 01 2022 Paul <devnoname120@gmail.com> - 0.7-1
- xkb-qwerty-fr (0.7) unstable; urgency=low

    * Layout: Added a new math mode (not available on Linux due to xkb
      limitations) which allows to type mathematical formulas conveniently.
      It can be activated by pressing m.
    * Layout: Added capital sharp s: ẞ (Germany).
    * Layout: Added extra ˚ characters: D̊, d̊, E̊, e̊, G̊, g̊, I̊, i̊, O̊,
      o̊, Q̊, q̊, S̊, s̊, V̊, v̊, W̊, X̊, x̊, Y̊.
    * Layout: Added above dot ˙ (Lithuanian, Polish, Turkish).
    * Layout: Added breve ˘ (Romanian, Turkish).
    * Layout: Added reverted breve ̑ (Serbian, Croatian).
    * Layout: Added d with stroke: đ, Đ (Faroese, Icelandic).
    * Layout: Added thorn: Þ/þ (Icelandic).
    * Layout: Added ŋ/Ŋ (Sami) on the ogonek dead key layer.
    * Layout: Moved ø/Ø from \ to 0 to be easier to learn (Danish, Faroese,
      Norwegian).
    * Layout: Moved € from 5 to 4.
    * Layout: Moved the caron ¯ from 5 to 4.
    * Layout: Moved the currency dead key ¤ from 5 to 4.
    * MacOS: Added a workaround for a macOS bug that swaps keys between ANSI
      and ISO keyboards.

* Mon Nov 15 2021 Paul <devnoname120@gmail.com> - 0.6-1
- xkb-qwerty-fr (0.6) unstable; urgency=low

    * Layout: Moved circumflex keys ê, û, î, ô one column to the left.
    * Layout: Removed ŷ key (it can still be done with the dead key ^).
    * Layout: Removed broken pipe (¦).
    * Layout: Replaced ± with ≈.
    * Layout: Replaced ¶ with acute accent dead key (´).
    * Layout: Replaced § with ring dead key (˚).
    * Layout: Replaced ring dead key (˚) with ellipsis (…).
    * Layout: Replaced ring (°) with middle punct (·)
    * Layout: Replaced irony punctuation (⸮) with typographic apostrophe (’).
    * Layout: Added greek dead key, removed greek letters from direct access.
    * Layout: Added currency dead key.
    * Layout: Added non-breaking, and narrow non-breaking spaces.
    * MacOS: Finish implementing all the dead keys.
    * Fixed debian package building.

* Wed Nov 10 2012 Julien Blitte <julien.blitte@gmail.com> - 0.5-1
- xkb-qwerty-fr (0.5) unstable; urgency=low

    * Bug fixed: trigger was missing with xkb files.
    * Extras xml used.
    * Layout: Ironic point updated.

* Sat May 01 2010 Julien Blitte <julien.blitte@gmail.com> - 0.4-1
- xkb-qwerty-fr (0.4) unstable; urgency=low

    * Layout: Added useful greek letters, math symbols.
    * Layout: Thorn letter moved and capital removed.
    * Layout: Added ogonek diacritic.
    * Keymap is now full.
    * Now based on basic US layout.

* Mon Nov 02 2009 Julien Blitte <julien.blitte@gmail.com> - 0.3-1
- xkb-qwerty-fr (0.3) unstable; urgency=low

    * Bug fixed: dpkg-reconfigure was not working properly.

* Sat Apr 25 2009 Julien Blitte <julien.blitte@gmail.com> - 0.2-1
- xkb-qwerty-fr (0.2) unstable; urgency=low

    * Compliant with evdev.
    * Added as a variant of us layouts.

* Wed Sep 24 2008 Julien Blitte <julien.blitte@gmail.com> - 0.1b-1
- xkb-qwerty-fr (0.1b) unstable; urgency=low

    * Initial Debian package.
    * Lintian 1.23.46 satisfied.
