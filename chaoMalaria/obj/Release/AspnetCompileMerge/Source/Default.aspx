<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="WebApplication6._Default" %>

<%@ Register assembly="System.Web.DataVisualization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" namespace="System.Web.UI.DataVisualization.Charting" tagprefix="asp" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <br />
    <div id="LoginDiv" runat="server" Visible="true">
        <asp:TextBox ID="PasswordTextBox" runat="server"></asp:TextBox>
        <asp:Button ID="LoginButton" runat="server" Text="Enter" OnClick="LoginButton_Click" />
    </div>
    <div id="MainDiv" runat="server" Visible="false"> 
        <div class="row">
        
        <div class="col-md-4">
            <h2>Upload</h2>
            <p>
                A blood sample image taken with a 100x microscope is perfect to run the analysis.  
            </p>
        </div>
        <div class="col-md-4">
            <h2>Process</h2>
            <p>
                Our image processing algorithms automatically analyze your sample.
            </p>
        </div>
        <div class="col-md-4">
            <h2>Results</h2>
            <p>
                You can instantly obtain a Malaria Probability Index at the end of the process.
            </p>
        </div>
    </div>

    <div class="jumbotron">
        <p class="lead">Image Processing Algorithm</p>
        <p>Select File &nbsp;<asp:FileUpload ID="FileUploader" runat="server"  accept='image/*'/></p>
        <p><asp:Button ID="Button1" class="btn btn-primary btn-lg" runat="server" Text="Upload image &raquo;" OnClick="Button1_Click" /></p>
        <p><asp:Label ID="Label1" runat="server" Text=""></asp:Label></p>
        <div  id="inputDiv"  runat="server" class="panel panel-info" style="display: none;">
            <div class="panel-heading">
                <h3 class="panel-title">Input image</h3>
            </div>
            <div class="panel-body">
                <asp:Image ID="Image1" class="img-responsive col-lg-10"  runat="server" />
            </div>
        </div>
         <div  id="outputDiv" runat="server" class="panel panel-primary" style="display: none;">
            <div class="panel-heading">
                <h3 class="panel-title">Output image</h3>
            </div>
            <div class="panel-body">
                <asp:Image ID="Image2" class="img-responsive col-lg-10"  runat="server" />
            </div>
        </div>
    </div>
    <p>
        <ul class="nav nav-tabs">
            <li class="active"><a href="#home" data-toggle="tab" aria-expanded="true">Results</a></li>
            <li class=""><a href="#profile" data-toggle="tab" aria-expanded="false">Stats for Nerds</a></li>
            <li class="disabled"><a>Share</a></li>
        </ul>
            <div id="myTabContent" class="tab-content">
                <div class="tab-pane fade active in" id="home">
                    <table class="table table-striped table-hover ">
                    <thead>
                    <tr>
                        <th>Description</th>
                        <th>Amount</th>
                    </tr>
                    </thead>
                    <tbody>
                        <tr class="danger">
                        <td><span class="label label-primary">Red cells detected</span></td>
                        <td><asp:Label ID="LabelRed" runat="server" Text="0"></asp:Label></td>
                    </tr>
                    <tr>
                        <td><span class="label label-info">White cells detected</span></td>
                        <td><asp:Label ID="LabelWhite" runat="server" Text="0"></asp:Label></td>
                    </tr>
                    <tr class="success">
                        <td><span class="label label-warning">Platelet cells detected</span></td>
                        <td><asp:Label ID="LabelPlatelet" runat="server" Text="0"></asp:Label></td>
                    </tr>

                    <tr class="warning">
                        <td><span class="label label-danger"> Malaria detected</span></td>
                        <td><asp:Label ID="LabelMalaria" runat="server" Text="0"></asp:Label></td>
                    </tr>
                    </tbody>
                    </table> 
                </div>
                <div class="tab-pane fade" id="profile">
                    <p> <asp:Label ID="Label2" runat="server" Text=""></asp:Label></p> 
                    <p> 
                        <div class="panel panel-danger">
                            <div class="panel-heading">
                            <h3 class="panel-title">Image histogram</h3>
                            </div>
                            <div class="panel-body">
                                <asp:Chart ID="Chart1" class="img-responsive col-lg-10" runat="server" Width="975px">
                                    <series>
                                        <asp:Series Name="Series1" YValuesPerPoint="2">
                                        </asp:Series>
                                    </series>
                                    <chartareas>
                                        <asp:ChartArea Name="ChartArea1">
                                        </asp:ChartArea>
                                    </chartareas>
                                </asp:Chart>
                            </div>
                        </div>
                    </p>
                </div>
            </div>
    </p>



  </div>
</asp:Content>
