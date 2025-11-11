class EmbeddedGraph(BaseModel):
  graph_coordinates =   None
  graph_description = None 
  axes_labels =  None
  axes_units = None
def graph_localizer(im,graph_localization_strings): -> :EmbeddedGraph
  embedded_graphs = [embedded_graph1,...]
  return embedded_graphs
def graph_understander():
  ...
def graph_localizer_and_understander(im, page_meta_description,graph_localization_strings, question):
  
  #TODO: do we want to grab multiple graphs? 
  embedded_graphs = graph_localizer(im,page_meta_description,graph_localization_strings)
  graph_ims = []
  for graphi_coordinates:
    graph_im = image_cutter(im, graph_coordinates)
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
