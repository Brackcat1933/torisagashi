my @words = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0");

print "Content-Type: text/html; charset=Shift_JIS\n\n";
print "<html>";
print "<head><title>サンプル</title></head>";
print "<body>";

my $cnt1 = 0;
my $cnt2 = 0;
my $cnt3 = 0;
my $cnt4 = 0;
my $cnt5 = 0;
my $cnt6 = 0;
my $cnt7 = 0;
my $cnt8 = 0;

while ( $cnt1 < 62 ) {
    while ( $cnt2 < 62 ) {
        while ( $cnt3 < 62 ) {
            while ( $cnt4 < 62 ){
                while ( $cnt5 < 62 ){
                    while ( $cnt6 < 62 ) {
                         while ( $cnt7 < 62 ) {
                            while ( $cnt8 < 62 ){
                                $tripkey = "#$words[$cnt1]$words[$cnt2]$words[$cnt3]$words[$cnt4]$words[$cnt5]$words[$cnt6]$words[$cnt7]$words[$cnt8]";  # トリップキー文字列（# 付き）
                                $tripkey = substr $tripkey, 1;
                                $salt = substr $tripkey . "H.", 1, 2;
                                $salt =~ s/[^\.-z]/\./g;
                                $salt =~ tr/:;<=>?@[\\]^_`/A-Ga-f/;
                                $trip = crypt $tripkey, $salt;
                                $trip = substr $trip, -10;
                                $trip = "#$words[$cnt1]$words[$cnt2]$words[$cnt3]$words[$cnt4]$words[$cnt5]$words[$cnt6]$words[$cnt7]$words[$cnt8]" . "◆"  . $trip;
                                print "<p>" $trip, "</p>\n";
                                
                                $cnt8++;
                            }
                            $cnt8 = 1;
                            $cnt7++;
                        }
                        $cnt7 = 1;
                        $cnt6++;
                    }
                    $cnt6 = 1;
                    $cnt5++;
                }
                $cnt5 = 1;
                $cnt4++;
            }
            $cnt4 = 1;
            $cnt3++;
        }
        $cnt3 = 1;
        $cnt2++;
    }
    $cnt2 = 1;
    $cnt1++;
}
print "<p>初めてのCGI。</p>";
print "</body>";
print "</html>";
exit;
