// Help from http://bl.ocks.org/mbostock/4062045

var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var simulation = d3.forceSimulation()
    .force("charge", d3.forceManyBody().strength(-2000))
    .force("link", d3.forceLink().id(function(d) { return d.id; }))
    .force("text", d3.forceLink().id(function(d) { return d.id; }))
    .force("x", d3.forceX(width / 2))
    .force("y", d3.forceY(height / 2));
  //  .on("tick", ticked);

d3.json("graph.json", function(error, graph) {
  if (error) throw error;

  var link = svg.append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
    .attr("stroke-width", function(d) { return 2.5; })
    .style("marker-end",  "url(#suit)");
    //.attr("xlink:href",function(d) { return d.value; })
    //link.append().text(function(d) { return d.value; });


// http://stackoverflow.com/questions/23470330/adding-label-to-the-links-in-d3-force-directed-graph
  var linkText = svg.append("g")
      .attr("class", "link-label")
      .selectAll("line")
      .data(graph.links)
      .enter().append("text")
      .attr("font-family", "Arial, Helvetica, sans-serif")
      .attr("fill", "Black")
      .style("font", "bold 14px Arial")
      .attr("dy", ".35em")
      .attr("text-anchor", "middle")
      .text(function(d) {
          return d.value;
      });

  var node = svg.append("g")
      .attr("class", "nodes")
      .selectAll("circle")
      .data(graph.nodes)
      .enter().append("circle")
      .attr("r",
      function(d) {if (d.group == 1) {return 30} else {return 20} })
      .attr("fill", function(d) { if (d.group == 1) {return '#2D3590'} else {return '#B9BFFF'}; })
      .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));

      node.append("text")
            .attr("dx", 10)
            .attr("dy", ".35em")
            .text(function(d) { return d.id });

//Clicking on nodes

var path = [];

  node.on("click", function(d) {
    if (d3.select(this).attr("fill") == '#2D3590') {
      // Do Nothing
          }

      else if (d3.select(this).attr("fill") == '#B9BFFF') {
        d3.select(this)
        .attr("fill","lightcoral");
        path.push(d);
        console.log(path);
              //.style("fill","lightcoral")
              //.style("stroke","red");
      }
      else {
        d3.select(this)
              .attr("fill",'#B9BFFF');

          var index = path.indexOf(d);
          path.splice(index,1);
          console.log(path);
            //  .style("stroke","blue");

      }


      });


  simulation
      .nodes(graph.nodes)
      .on("tick", ticked);

  simulation.force("link")
      .links(graph.links);

  function ticked() {
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
    linkText
        .attr("x", function(d) {
                return ((d.source.x + d.target.x)/2);
            })
        .attr("y", function(d) {
                return ((d.source.y + d.target.y)/2);
            });
  }

// From http://www.coppelia.io/2014/07/an-a-to-z-of-extra-features-for-the-d3-force-layout/
  svg.append("defs").selectAll("marker")
      .data(["suit", "licensing", "resolved"])
    .enter().append("marker")
      .attr("id", function(d) { return d; })
      .attr("viewBox", "0 -5 10 10")
      .attr("refX", 25)
      .attr("refY", 0)
      .attr("markerWidth", 6)
      .attr("markerHeight", 6)
      .attr("orient", "auto")
    .append("path")
      .attr("d", "M0,-5L10,0L0,5 L10,0 L0, -5")
      .style("stroke", "#000000")
      .style("opacity", "0.5");

      $("button").click(function(){
        if (path.length == 0) {
        console.log('hello'); }
      });

});

function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
