form pitchEst
  sentence difonos
  sentence filename
endform
sound = Read from file... 'filename$'
Rename: "original"
selectObject(sound)
manipulation = To Manipulation: 0.01, 75, 600
pitchtier = Extract pitch tier
original = Copy: "old"
points = Get number of points
selectObject(original)
total = Get total duration
cantDifonos = 'difonos$'
for p to points  
  if p = 1
    f = p
    t = Get value at index: p 
  else
    f = Get value at index: p - 1
    t = Get time from index: p
  endif
  if t > ((0.60 + log10(cantDifonos)/10) * total)
    selectObject(pitchtier)
    Remove point: p
    val = f * 1.1
    if val > 260
      val = f * 0.4
    endif
    Add point: t, val
  endif
endfor
selectObject(pitchtier, manipulation)
Replace pitch tier
selectObject(manipulation)
new_sound = Get resynthesis (overlap-add)
removeObject(original, pitchtier, manipulation)
selectObject(new_sound)
Rename: "modified"
Write to WAV file... 'filename$'
