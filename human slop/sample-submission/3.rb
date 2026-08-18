gets.to_i.times{|i|i=89+i*75;puts 3.times.sum(''){r=i%47;i/=47;'bcdgjklmnr'[r/5]+'aeiou'[r%5]}.capitalize}
