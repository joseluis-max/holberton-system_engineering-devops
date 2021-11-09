#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:|to:|flags:)([^\]]+)/).join(",")
# puts ARGV[0].scan(/\[from:(\w+|\+?\d+)\]/).join 
# puts ARGV[0].scan(/\[to:(\w+|\+?\d+)\]/).join
# puts ARGV[0].scan(/\[flags:(-?\d:?)(-?\d:?)(-?\d:?)(-?\d:?)(-?\d:?)\]/).join

#/\[(from:|to:|flags:)\]/