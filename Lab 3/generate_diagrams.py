import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Arc

def draw_comp_icon(ax, x, y, border='#4A5568'):
    w, h = 0.38, 0.26
    main = Rectangle((x, y), w, h, facecolor='#FFFFFF', edgecolor=border, linewidth=1.2, zorder=6)
    ax.add_patch(main)
    tw = w * 0.42
    th = h * 0.22
    t1 = Rectangle((x - tw*0.5, y + h*0.60), tw, th, facecolor='#E2E8F0', edgecolor=border, linewidth=0.9, zorder=7)
    t2 = Rectangle((x - tw*0.5, y + h*0.18), tw, th, facecolor='#E2E8F0', edgecolor=border, linewidth=0.9, zorder=7)
    ax.add_patch(t1)
    ax.add_patch(t2)

def draw_layer(ax, x, y, w, h, name, color_bg, color_border, tab_w=2.9):
    layer = FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0.0",
                           facecolor=color_bg, edgecolor=color_border, linewidth=1.4, linestyle='--', zorder=1)
    ax.add_patch(layer)
    th = 0.38
    tab = Rectangle((x, y + h - th), tab_w, th, facecolor=color_border, edgecolor=color_border, zorder=2)
    ax.add_patch(tab)
    ax.text(x + tab_w/2, y + h - th/2, name, ha='center', va='center', fontsize=9.0, fontweight='bold', color='#FFFFFF', zorder=3)

def draw_component(ax, x, y, w, h, name, sub="", bg='#FFFDF5', border='#B7791F'):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.08",
                         facecolor=bg, edgecolor=border, linewidth=1.5, zorder=4)
    ax.add_patch(box)
    draw_comp_icon(ax, x + w - 0.50, y + h - 0.38, border=border)
    ax.text(x + w/2, y + h - 0.20, "<<component>>", ha='center', va='center',
            fontsize=8, fontstyle='italic', color='#718096', zorder=5)
    ax.text(x + w/2, y + h*0.56 if sub else y + h*0.48, name, ha='center', va='center',
            fontsize=10.0, fontweight='bold', color='#1A202C', zorder=5, wrap=True)
    if sub:
        ax.text(x + w/2, y + 0.22, sub, ha='center', va='center',
                fontsize=7.3, color='#4A5568', zorder=5)

def draw_port(ax, x, y):
    p = Rectangle((x - 0.08, y - 0.08), 0.16, 0.16, facecolor='#FFFFFF', edgecolor='#2B6CB0', linewidth=1.2, zorder=8)
    ax.add_patch(p)

def draw_assembly_v(ax, top_x, top_y, btm_x, btm_y, cy, name, protocol="", label_side='right', label_offset=0.22):
    ax.plot([top_x, top_x], [top_y, cy], color='#2B6CB0', linewidth=1.4, zorder=9)
    socket = Arc((top_x, cy), 0.34, 0.34, angle=0, theta1=180, theta2=360, edgecolor='#2B6CB0', linewidth=2.0, zorder=11)
    ax.add_patch(socket)
    ax.plot([btm_x, btm_x], [btm_y, cy], color='#2B6CB0', linewidth=1.4, zorder=9)
    ball = Circle((btm_x, cy), 0.11, facecolor='#FFFFFF', edgecolor='#2B6CB0', linewidth=1.8, zorder=12)
    ax.add_patch(ball)
    lbl = f"<<interface>>\n{name}\n[{protocol}]" if protocol else f"<<interface>>\n{name}"
    lx = top_x + label_offset if label_side == 'right' else top_x - label_offset
    ha = 'left' if label_side == 'right' else 'right'
    ax.text(lx, cy, lbl, ha=ha, va='center', fontsize=7.2, fontweight='bold', color='#1A365D',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#F7FAFC', edgecolor='#CBD5E0', alpha=0.96), zorder=15)

def draw_assembly_h(ax, left_x, left_y, right_x, right_y, cx, name, protocol="", label_side='above', label_offset=0.38):
    ax.plot([left_x, cx], [left_y, left_y], color='#2B6CB0', linewidth=1.4, zorder=9)
    socket = Arc((cx, left_y), 0.34, 0.34, angle=0, theta1=90, theta2=270, edgecolor='#2B6CB0', linewidth=2.0, zorder=11)
    ax.add_patch(socket)
    ax.plot([right_x, cx], [right_y, right_y], color='#2B6CB0', linewidth=1.4, zorder=9)
    ball = Circle((cx, right_y), 0.11, facecolor='#FFFFFF', edgecolor='#2B6CB0', linewidth=1.8, zorder=12)
    ax.add_patch(ball)
    lbl = f"<<interface>> {name}\n[{protocol}]" if protocol else f"<<interface>> {name}"
    ly = left_y + label_offset if label_side == 'above' else left_y - label_offset
    ax.text(cx, ly, lbl, ha='center', va='center', fontsize=7.2, fontweight='bold', color='#1A365D',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#F7FAFC', edgecolor='#CBD5E0', alpha=0.96), zorder=15)

def draw_legend(ax, leg_x, leg_y, leg_w, leg_h):
    leg_box = Rectangle((leg_x, leg_y), leg_w, leg_h, facecolor='#EDF2F7', edgecolor='#CBD5E0', linewidth=1.0, zorder=2)
    ax.add_patch(leg_box)
    ax.text(leg_x + 0.2, leg_y + 0.17, "UML 2.5 Legend:", fontsize=8, fontweight='bold', color='#2D3748', zorder=3)
    
    draw_comp_icon(ax, leg_x + 1.8, leg_y + 0.05, border='#4A5568')
    ax.text(leg_x + 2.3, leg_y + 0.17, "Component Box", fontsize=7.5, color='#2D3748', zorder=3)
    
    c1 = Circle((leg_x + 4.5, leg_y + 0.17), 0.08, facecolor='#FFFFFF', edgecolor='#2B6CB0', linewidth=1.5, zorder=3)
    ax.add_patch(c1)
    ax.plot([leg_x + 4.2, leg_x + 4.5], [leg_y + 0.17, leg_y + 0.17], color='#2B6CB0', linewidth=1.2, zorder=3)
    ax.text(leg_x + 4.7, leg_y + 0.17, "Provided Interface (Ball)", fontsize=7.5, color='#2D3748', zorder=3)

    ax.plot([leg_x + 7.4, leg_x + 7.7], [leg_y + 0.17, leg_y + 0.17], color='#2B6CB0', linewidth=1.2, zorder=3)
    s1 = Arc((leg_x + 7.7, leg_y + 0.17), 0.20, 0.20, angle=0, theta1=270, theta2=90, edgecolor='#2B6CB0', linewidth=1.8, zorder=3)
    ax.add_patch(s1)
    ax.text(leg_x + 7.9, leg_y + 0.17, "Required Interface (Socket)", fontsize=7.5, color='#2D3748', zorder=3)

    ax.plot([leg_x + 10.7, leg_x + 10.9], [leg_y + 0.17, leg_y + 0.17], color='#2B6CB0', linewidth=1.2, zorder=3)
    c2 = Circle((leg_x + 10.9, leg_y + 0.17), 0.08, facecolor='#FFFFFF', edgecolor='#2B6CB0', linewidth=1.5, zorder=4)
    ax.add_patch(c2)
    s2 = Arc((leg_x + 10.9, leg_y + 0.17), 0.20, 0.20, angle=0, theta1=270, theta2=90, edgecolor='#2B6CB0', linewidth=1.8, zorder=3)
    ax.add_patch(s2)
    ax.plot([leg_x + 10.9, leg_x + 11.2], [leg_y + 0.17, leg_y + 0.17], color='#2B6CB0', linewidth=1.2, zorder=3)
    ax.text(leg_x + 11.35, leg_y + 0.17, "Assembly Connector", fontsize=7.5, color='#2D3748', zorder=3)

    ax.annotate("", xy=(leg_x + 14.1, leg_y + 0.17), xytext=(leg_x + 13.5, leg_y + 0.17),
                arrowprops=dict(arrowstyle="->,head_width=0.25,head_length=0.3", linestyle="--",
                                color='#718096', linewidth=1.2))
    ax.text(leg_x + 14.25, leg_y + 0.17, "<<use>> Dependency", fontsize=7.5, color='#2D3748', zorder=3)

def create_component_diagram_ps28(output_png, output_pdf):
    fig, ax = plt.subplots(figsize=(17, 12.2), dpi=300)
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 12.2)
    ax.axis('off')
    
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    # Title Banner
    banner = FancyBboxPatch((0.5, 10.75), 16.0, 1.15, boxstyle="round,pad=0.03,rounding_size=0.08",
                            facecolor='#1A365D', edgecolor='#2B6CB0', linewidth=1.5, zorder=2)
    ax.add_patch(banner)
    ax.text(8.5, 11.55, "PES UNIVERSITY • DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING",
            ha='center', va='center', fontsize=12.5, fontweight='bold', color='#E2E8F0', zorder=3)
    ax.text(8.5, 11.15, "UE23CS341A - Software Engineering Lab 3 • UML 2.5 Component Diagram",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#FFFFFF', zorder=3)
    ax.text(8.5, 10.88, "Scenario: Problem Statement #28 — Inter-City Freight Load Matching Marketplace | Architectural Pattern: Layered Architecture",
            ha='center', va='center', fontsize=9.5, color='#CBD5E0', zorder=3)

    # Student Info Banner
    info_box = FancyBboxPatch((0.5, 10.28), 16.0, 0.38, boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor='#EDF2F7', edgecolor='#CBD5E0', linewidth=1.0, zorder=2)
    ax.add_patch(info_box)
    ax.text(1.0, 10.47, "STUDENT: Vismay Shyam Vasishta", fontsize=8.5, fontweight='bold', color='#2D3748', zorder=3)
    ax.text(5.8, 10.47, "SRN: PES2UG24AM184", fontsize=8.5, fontweight='bold', color='#2D3748', zorder=3)
    ax.text(10.2, 10.47, "TEAM: 28 (CODEVERSE)", fontsize=8.5, fontweight='bold', color='#2D3748', zorder=3)
    ax.text(14.2, 10.47, "LAB: Lab 3 (Arch & Components)", fontsize=8.5, fontweight='bold', color='#2D3748', zorder=3)

    # Layers (tab_w = 2.8 so it never touches any connectors)
    draw_layer(ax, 0.6, 7.95, 15.8, 2.15, "Presentation Layer", '#F7FAFC', '#4A5568', tab_w=2.8)
    draw_layer(ax, 0.6, 2.75, 15.8, 5.0, "Business / Application Logic Layer", '#F7FAFC', '#2B6CB0', tab_w=3.4)
    draw_layer(ax, 0.6, 0.45, 15.8, 2.15, "Data / Persistence Layer", '#F7FAFC', '#2F855A', tab_w=2.8)

    # 1. Presentation Layer Component
    draw_component(ax, 3.2, 8.2, 10.6, 1.45,
                   name="Shipper & Carrier Web / Mobile Portal Component",
                   sub="Responsive Web/Mobile GUI: Freight Shipment Posting, Bid Submissions, Live Tracking & e-POD Upload",
                   bg='#EBF8FF', border='#3182CE')
    draw_port(ax, 4.8, 8.2)
    draw_port(ax, 8.5, 8.2)
    draw_port(ax, 12.2, 8.2)

    # 2. Business Layer Components (5 components)
    # Comp 1: Shipment Order Manager
    draw_component(ax, 0.9, 5.4, 4.3, 1.7,
                   name="Shipment Order Manager Component",
                   sub="Shipment Lifecycle, Listing Validation, State Machine\n& Milestone Tracking (FR-002, FR-003)",
                   bg='#FEFCBF', border='#D69E2E')
    draw_port(ax, 4.8, 7.1)
    draw_port(ax, 5.2, 6.2)
    draw_port(ax, 3.0, 5.4)

    # Comp 2: Carrier Bidding & Matching Service
    draw_component(ax, 6.4, 5.4, 4.4, 1.7,
                   name="Carrier Bidding & Matching Component",
                   sub="Auction Timeframe Engine, Carrier Verification\n& Bid Selection Optimization (FR-001, FR-003)",
                   bg='#FEFCBF', border='#D69E2E')
    draw_port(ax, 8.5, 7.1)
    draw_port(ax, 6.4, 6.2)

    # Comp 3: e-POD Verification Service
    draw_component(ax, 11.6, 5.4, 4.4, 1.7,
                   name="e-POD Verification Service Component",
                   sub="Digital Signature Validation, GPS Timestamping,\nDelivery Inspection Sign-off (FR-004)",
                   bg='#FEFCBF', border='#D69E2E')
    draw_port(ax, 12.2, 7.1)
    draw_port(ax, 11.6, 5.9)

    # Comp 4: Escrow & Payment Service Component
    draw_component(ax, 1.2, 2.95, 5.8, 1.6,
                   name="Escrow & Payment Service Component",
                   sub="Financial Escrow Vault, Milestone Payment Disbursement\n<=60s Auto-Disburse SLA Verification (NFR-001)",
                   bg='#FEEBC8', border='#DD6B20')
    draw_port(ax, 3.0, 4.55)
    draw_port(ax, 7.0, 3.75)
    draw_port(ax, 4.2, 2.95)

    # Comp 5: Shipment Event Notification Component
    draw_component(ax, 9.8, 2.95, 5.8, 1.6,
                   name="Shipment Event Notification Component",
                   sub="Real-time Dispatcher: Outbid Alerts, e-POD Verification,\nPayment Release & Status Push Notifications (FR-005)",
                   bg='#E9D8FD', border='#805AD5')
    draw_port(ax, 9.8, 3.9)
    draw_port(ax, 12.6, 2.95)

    # 3. Data Layer Component
    draw_component(ax, 3.2, 0.75, 10.6, 1.45,
                   name="Database & Secure Audit Repository Component",
                   sub="Relational PostgreSQL Store: Shipments, Bids, Escrow Ledger, Audit Trail & RBAC (NFR-002)",
                   bg='#F0FFF4', border='#38A169')
    draw_port(ax, 4.2, 2.2)
    draw_port(ax, 12.6, 2.2)

    # ---------------- CONNECTORS ----------------
    # UI -> Shipment Order: IShipmentOrder (placed on right side of port 4.8)
    draw_assembly_v(ax, 4.8, 8.2, 4.8, 7.1, 7.65, "IShipmentOrder", "REST / HTTPS JSON", label_side='right', label_offset=0.22)

    # UI -> Bidding: IBidAuction
    draw_assembly_v(ax, 8.5, 8.2, 8.5, 7.1, 7.65, "IBidAuction", "WebSocket / HTTPS", label_side='right', label_offset=0.22)

    # UI -> e-POD: IDeliveryProof
    draw_assembly_v(ax, 12.2, 8.2, 12.2, 7.1, 7.65, "IDeliveryProof", "HTTPS Multipart / REST", label_side='right', label_offset=0.22)

    # Shipment Order <-> Bidding: ICarrierSelection (cx = 5.8, label above)
    draw_assembly_h(ax, 5.2, 6.2, 6.4, 6.2, 5.8, "ICarrierSelection", "In-Process gRPC", label_side='above', label_offset=0.38)

    # Order Manager <-> Escrow Payment: IPaymentEscrow [Given in handout!]
    draw_assembly_v(ax, 3.0, 5.4, 3.0, 4.55, 4.98, "IPaymentEscrow", "Internal Financial RPC [Given]", label_side='right', label_offset=0.22)

    # e-POD Verification -> Escrow & Payment: auto-release (<60s)
    ax.annotate("", xy=(7.0, 3.75), xytext=(11.6, 5.9),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.4", linestyle="--",
                                color='#C53030', linewidth=1.5, connectionstyle="arc3,rad=-0.12"), zorder=8)
    ax.text(9.3, 5.0, "<<use>> Trigger Milestone Auto-Disbursement\n[Within 60s SLA - NFR-001]",
            ha='center', va='center', fontsize=7.2, fontweight='bold', color='#C53030',
            bbox=dict(boxstyle='round,pad=0.12', facecolor='#FFF5F5', edgecolor='#FEB2B2', alpha=0.96), zorder=14)

    # Escrow -> Notification Component
    ax.annotate("", xy=(9.8, 3.9), xytext=(7.0, 3.3),
                arrowprops=dict(arrowstyle="->,head_width=0.25,head_length=0.35", linestyle="--",
                                color='#805AD5', linewidth=1.3, connectionstyle="arc3,rad=0.08"), zorder=8)
    ax.text(8.4, 3.35, "<<use>> publishEvent() [FR-005]",
            ha='center', va='center', fontsize=7.0, fontstyle='italic', color='#553C9A',
            bbox=dict(boxstyle='square,pad=0.08', facecolor='#FAF5FF', edgecolor='#E9D8FD', alpha=0.9), zorder=14)

    # Business Layer -> Database Layer: IDataAccess (label on right side of x=4.2 and x=12.6)
    draw_assembly_v(ax, 4.2, 2.95, 4.2, 2.2, 2.58, "IDataAccess", "TLS Encrypted SQL / Pool", label_side='right', label_offset=0.22)
    draw_assembly_v(ax, 12.6, 2.95, 12.6, 2.2, 2.58, "IDataAccess", "TLS Encrypted SQL / Pool", label_side='right', label_offset=0.22)

    # Legend
    draw_legend(ax, 0.6, 0.05, 15.8, 0.35)

    plt.tight_layout()
    plt.savefig(output_png, dpi=300, bbox_inches='tight')
    plt.savefig(output_pdf, bbox_inches='tight')
    plt.close()
    print(f"Generated {output_png} and {output_pdf}")

def create_component_diagram_coffee_kiosk(output_png, output_pdf):
    fig, ax = plt.subplots(figsize=(17, 12.2), dpi=300)
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 12.2)
    ax.axis('off')
    
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    # Title Banner
    banner = FancyBboxPatch((0.5, 10.75), 16.0, 1.15, boxstyle="round,pad=0.03,rounding_size=0.08",
                            facecolor='#7B341E', edgecolor='#9C4221', linewidth=1.5, zorder=2)
    ax.add_patch(banner)
    ax.text(8.5, 11.55, "PES UNIVERSITY • DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING",
            ha='center', va='center', fontsize=12.5, fontweight='bold', color='#FED7D7', zorder=3)
    ax.text(8.5, 11.15, "UE23CS341A - Software Engineering Lab 3 • UML 2.5 Component Diagram",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#FFFFFF', zorder=3)
    ax.text(8.5, 10.88, "Scenario: Self-Service Coffee Kiosk System (Handout Exercise) | Architectural Style: Layered Architecture",
            ha='center', va='center', fontsize=9.5, color='#FEEBC8', zorder=3)

    # Student Info Box
    info_box = FancyBboxPatch((0.5, 10.28), 16.0, 0.38, boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor='#EDF2F7', edgecolor='#CBD5E0', linewidth=1.0, zorder=2)
    ax.add_patch(info_box)
    ax.text(1.0, 10.47, "STUDENT: Vismay Shyam Vasishta", fontsize=8.5, fontweight='bold', color='#2D3748', zorder=3)
    ax.text(5.8, 10.47, "SRN: PES2UG24AM184", fontsize=8.5, fontweight='bold', color='#2D3748', zorder=3)
    ax.text(10.2, 10.47, "SECTION: 5th Sem CSE / AIML", fontsize=8.5, fontweight='bold', color='#2D3748', zorder=3)
    ax.text(14.2, 10.47, "LAB: Lab 3 (Architecture)", fontsize=8.5, fontweight='bold', color='#2D3748', zorder=3)

    # Layers
    draw_layer(ax, 0.6, 7.95, 15.8, 2.15, "Presentation Layer", '#FFFAF0', '#DD6B20', tab_w=2.8)
    draw_layer(ax, 0.6, 2.75, 15.8, 5.0, "Business / Application Logic Layer", '#F7FAFC', '#2B6CB0', tab_w=3.4)
    draw_layer(ax, 0.6, 0.45, 15.8, 2.15, "Data / Persistence Layer", '#F0FFF4', '#2F855A', tab_w=2.8)

    # 1. Presentation Layer
    draw_component(ax, 3.5, 8.2, 10.0, 1.45,
                   name="User Interface Component",
                   sub="Touchscreen GUI: Espresso, Americano, Latte | Small / Large Size Selection | Credit Card Payment Flow",
                   bg='#FFFAF0', border='#DD6B20')
    draw_port(ax, 8.5, 8.2)

    # 2. Business Layer (3 Components with wide horizontal spacing)
    # Payment Service Component (Left)
    draw_component(ax, 1.0, 5.0, 4.0, 1.9,
                   name="Payment Service Component",
                   sub="[Given Component 2]\nCredit Card POS Terminal Gateway, EMV/NFC Handling,\nPCI-DSS Cardholder Data Isolation",
                   bg='#FEEBC8', border='#DD6B20')
    draw_port(ax, 5.0, 5.95)

    # Order Manager Component (Center)
    draw_component(ax, 6.5, 5.0, 4.0, 1.9,
                   name="Order Manager Component",
                   sub="[Given Component 1]\nOrder State Machine, Drink Customization & Sizing,\nPricing Calculation & Workflow Coordination",
                   bg='#FEFCBF', border='#D69E2E')
    draw_port(ax, 8.5, 6.9)  # Top port for UI
    draw_port(ax, 6.5, 5.95) # Left port for Payment
    draw_port(ax, 10.5, 5.95) # Right port for Receipt
    draw_port(ax, 8.5, 5.0)  # Bottom port for Database

    # Receipt Printer Component (Right)
    draw_component(ax, 12.0, 5.0, 4.0, 1.9,
                   name="Receipt Printer Component",
                   sub="Hardware Abstraction & Spooling, ESC/POS Formatter,\nPrints Order Details, Timestamp, Total & Auth Code",
                   bg='#EBF8FF', border='#3182CE')
    draw_port(ax, 12.0, 5.95)

    # 3. Data Layer
    draw_component(ax, 3.5, 0.75, 10.0, 1.45,
                   name="Database Component",
                   sub="Local Embedded Storage (SQLite): Beverage Menu Catalog, Size Pricing Rates, Transaction Logs & Audits",
                   bg='#F0FFF4', border='#38A169')
    draw_port(ax, 8.5, 2.2)

    # ---------------- INTERFACES & CONNECTORS ----------------
    # 1. Order Interface: UI Component <-> Order Manager Component
    draw_assembly_v(ax, 8.5, 8.2, 8.5, 6.9, 7.55, "Order Interface (IOrderProcessing)", "Local In-Process IPC / API", label_side='right', label_offset=0.22)

    # 2. Payment Interface: Order Manager <-> Payment Service (GIVEN IN HANDOUT!)
    draw_assembly_h(ax, 5.0, 5.95, 6.5, 5.95, 5.75, "Payment Interface\n(IPaymentProcessing)", "Secure IPC / POS API [Given]", label_side='above', label_offset=0.42)

    # 3. Receipt Interface: Order Manager <-> Receipt Printer Component
    draw_assembly_h(ax, 10.5, 5.95, 12.0, 5.95, 11.25, "Receipt Interface\n(IReceiptPrinting)", "ESC/POS Serial/USB Driver", label_side='above', label_offset=0.42)

    # 4. Database Interface: Order Manager <-> Database Component
    draw_assembly_v(ax, 8.5, 5.0, 8.5, 2.2, 3.60, "Database Interface (IDataAccess)", "Local SQL / ORM Queries", label_side='right', label_offset=0.22)

    # Data Flow Annotations
    ax.text(8.5, 4.35, "Data Flow: [1] Customer Order -> [2] Order Manager -> [3] Card Payment -> [4] DB Log -> [5] Receipt Print",
            ha='center', va='center', fontsize=8, fontweight='bold', color='#2B6CB0',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#EBF8FF', edgecolor='#BEE3F8', alpha=0.96), zorder=14)

    # Legend
    draw_legend(ax, 0.6, 0.05, 15.8, 0.35)

    plt.tight_layout()
    plt.savefig(output_png, dpi=300, bbox_inches='tight')
    plt.savefig(output_pdf, bbox_inches='tight')
    plt.close()
    print(f"Generated {output_png} and {output_pdf}")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    create_component_diagram_ps28(os.path.join(base_dir, "Deliverable_1_Component_Diagram.png"),
                                 os.path.join(base_dir, "Deliverable_1_Component_Diagram.pdf"))
    create_component_diagram_coffee_kiosk(os.path.join(base_dir, "Coffee_Kiosk_Component_Diagram.png"),
                                          os.path.join(base_dir, "Coffee_Kiosk_Component_Diagram.pdf"))
