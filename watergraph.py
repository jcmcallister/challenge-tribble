# Water inside a bar graph

"""	given any bar graph and it's axes intervals, find out how much water you could fit
	 inside any complete valleys (not including "runoff" down any steep sides)
	 """

"""thoughts:
		do an O(n) loop over the graph's x values, looking at y(x) per point
			record all potential valley peaks by matching
				if all points between points y1 and y2 are less than y1 and y2
					you have a valley!
					record the valley's peaks in a list

			run over the list of valley peaks and get all y(x) points between x2-x1
				do basic rectangle products & addition
					(given any low point p between the min of x2/x1 values)
						we assume that any water contained in a valley above this min(x1,x2) "runs off"
					waterDepthTotal += y( min(x2,x1) ) - p for every low point p between 2 peaks


"""