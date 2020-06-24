# what are my chances of randomly being selected as one of the 9? 9 out of 100?
my_id = 5 
job_applicants = (1..10).to_a
open_positions = 2

combos = job_applicants.combination(open_positions).to_a

occurrences_of_my_id = combos.count {|combo| combo.include? my_id}
my_chances = occurrences_of_my_id.to_f / combos.length

puts "#{open_positions} positions / #{job_applicants.length} job applicants = #{open_positions.to_f / job_applicants.length}"
puts "#{occurrences_of_my_id} / #{combos.length} = #{my_chances}"



def n_choose_r (n, r)
  return 1 if (n == 0 || n == r)
  return n_factorial(n) / (n_factorial(r) * n_factorial(n - r))
end


def n_factorial (n)
  return Math.gamma(n+1).to_i
end


# p n_choose_r job_applicants, open_positions