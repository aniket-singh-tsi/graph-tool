import logging
logging.basicConfig(loglevel = logging.DEBUG) #TODO
... # function line number etc.
class EmbeddedGraph(BaseModel):
  graph_coordinates =   None
  graph_description = None 
  axes_labels =  None
  axes_units = None
class Bbox(BaseModel):
  ...
def draw_bbox_on_im(im,bbox_coordinates,bbox_color):
  ...
  return overlayed
def image_cutter(im,coords):
  ...
  return cut
def place_im_in_labeled_matplotlib(im,xlabels,ylabels):
  ...
  return out_im
def graph_localizer(im,graph_localization_strings): -> :EmbeddedGraph
  previous_coordinates = None
  highlighted_from_previous_output = None
  MAX_ITER = 5
  i = 0
  while True:
    logging.debug(f"iteration {i}")
    if i > MAX_ITER:
      break
    
    embedded_graph_or_done = llm_call(im, highlighted_from_previous_output, previous_coordinates,CUT_GRAPH_PROMPT)
    if isinstance(embedded_graph_or_done,bool) and embedded_graph_or_done:
      break
    embedded_graph = embedded_graph_or_done
    graph_coordinates = embedded_graph.graph_coordinates
    highlighted = draw_bbox_on_im(im,graph_coordinates)
    highlighted_from_previous_output,previous_coordinates = highlighted,graph_coordinates
    i += 1
  graph_im = image_cutter(im, graph_coordinates)
  MAX_VERIFY_ITER = 5
  while True:
    logging.debug(f"Axes verifying iteration {i}")
    if i > MAX_VERIFY_ITER:
      break
    gridded = place_im_in_labeled_matplotlib(graph_im,xgrid,xlabels,ygrid,ylabels)
    change_axes_or_done = llm_call(gridded_graph,im,VERIFY_AXES_PROMPT)
    if isinstance(change_axes_or_done,bool) and change_axes_or_done:
      break
    new_axes = change_axes_or_done
    xgrid = ...
    ygrid = ...
    ...
    
    
  return embedded_graph
def graph_manipulator():
  
def graph_understander(graph_ims,graph_descriptions,axes_labels,axes_units,question):
  
  ...
def graph_localizer_and_understander(im, page_meta_description,graph_localization_strings, question):
  
  #TODO: do we want to grab multiple graphs? 
  graph_ims,embedded_graphs = [graph_localizer(im,page_meta_description,graph_localization_string) for graph_localization_string in graph_localization_strings]
  graph_ims = []

    
  answer = graph_understander(graph_ims,question,graph_coordinates, graph_description, axes_labels,axes_units)
  


def test():
  im = read_image('Productinformation_Vaillant_350.pdf_page_176.png')
  page_meta_description = "...."
  graph_localization_string = "the question needs the graph explaining aroCollect volume flow"
  question = "Wie ist der Volumenstrom von einem aroCOLLECT bei einer Rotationsgeschwindigkeit von 500 rpm?"
  graph_localizer_and_understander(im,page_meta_description, graph_localization_string, question)

'''
xcoordinates: [-15,15]
ycoordinates: [0,8]
dscription: the graph contains 3 cases denoted by 3 different colors. case 1 is in brown represents 3 lines at temperatures 55,45,35  ...
'''
