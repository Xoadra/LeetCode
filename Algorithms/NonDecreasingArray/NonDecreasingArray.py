



""" Needs revision as this solution is heavly brute-forced """



def is_nondecreasing( nums ):
	highest = nums[ 0 ]
	subtracts = 0
	for idx in range( 1, len( nums ) ):
		print( 'Is ' + str( nums[ idx - 1 ] ) + ' greater than ' + str( nums[ idx ] ) + '?' )
		## Check if the following index exists as well as the previous index
		if idx + 1 < len( nums ) and subtracts < 2:
			## Are both of the adjacent index values to the current one larger?
			if nums[ idx - 1 ] > nums[ idx ] and nums[ idx ] <= nums[ idx + 1 ]:
				highest = nums[ idx + 1 ]
				## First value must be modified to be lower than the other two
				subtracts += 1
			## Is the highest larger than the next, but lower than the current?
			elif highest <= nums[ idx ] and highest > nums[ idx + 1 ]:
				nums[ idx + 1 ] = highest + 1
				highest = nums[ idx + 1 ]
				## Last value needs to become larger than the previous highest
				subtracts += 1
			## Might the current value be greater than the last highest or next?
			elif highest <= nums[ idx ] and nums[ idx ] > nums[ idx + 1]:
				nums[ idx ] = nums[ idx - 1 ] + 1
				highest = nums[ idx + 1 ]
				## Middle value is made smaller than the next, but not the first
				subtracts += 1
			## Do the following index values decrease relative to the previous?
			elif nums[ idx - 1 ] > nums[ idx ] and nums[ idx ] > nums[ idx + 1 ]:
				## Both the current and following value will require modification!
				print( 'It\'s false!' )
				return False
			## Values increase naturally to the next, so no changes necessary
			else:
				highest = nums[ idx ]
		## Has the array's final index value been reached and isn't the largest?
		elif highest > nums[ idx ] and subtracts < 2:
			nums[ idx ] = highest + 1
			highest = nums[ idx ]
			subtracts += 1
		## Was more than one modification to the array necessary thus far?
		print( 'What is subtracts at?  ' + str( subtracts) )
		if subtracts >= 2:
			print( 'It\'s false!' )
			return False
	## Only one or no modified values after iterating through the entire array
	print( 'It\'s true!' )
	return True



nums = [ 4, 2, 1 ]

is_nondecreasing( nums )


