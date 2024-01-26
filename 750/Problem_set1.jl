using LinearAlgebra


x = [1;0;0;0;]
y = [0;1;0;0;]
z = [0;0;1;0;]
w = [0;0;0;1;]

display(x*x')
display(x*y')
display(y*x')
display(y*y')
display(w*w')
# Define the states |+> and |->
plus = [1; 1] / sqrt(2)
minus = [1; -1] / sqrt(2)

# Define the states |+i> and |-i> (eigenstates of sigma_y)
plus_i = [1; im] / sqrt(2)
minus_i = [1; -im] / sqrt(2)

# Define the states |ψ> and |ϕ>
psi = (3 * plus + minus) / sqrt(10)
phi = (plus_i - 3 * minus_i) / sqrt(10)

# Calculate the density matrices for each state
rho_psi = (psi * psi') / 3  # Probability for |ψ> is 1/3
rho_phi = (phi * phi') * 2 / 3  # Probability for |ϕ> is 2/3
println("psi':")
display(psi')
println("psi:")
display(psi)
# Calculate the total density matrix ρM
rho_M = rho_psi + rho_phi

# Calculate the square of the density matrix ρM^2
rho_M_squared = rho_M^2

# Use display for pretty-printing the output
println("State |ψ>:")
display(psi)

println("\nState |ϕ>:")
display(phi)

println("\nDensity matrix ρM:")
display(rho_M)

println("\nSquare of the density matrix ρM^2:")
display(rho_M_squared)

